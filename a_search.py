import random
from pyamaze import maze, agent
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(m):
    # بداية عشوائية كل تشغيل
    start = random.choice(list(m.grid))

    goal = (1,1)

    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)

    open = PriorityQueue()
    open.put((f_score[start], start))

    aPath = {}

    while not open.empty():
        currCell = open.get()[1]

        if currCell == goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g = g_score[currCell] + 1
                temp_f = temp_g + h(childCell, goal)

                if temp_f < f_score[childCell]:
                    g_score[childCell] = temp_g
                    f_score[childCell] = temp_f
                    open.put((temp_f, childCell))
                    aPath[childCell] = currCell

    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return fwdPath, start

# التشغيل
if __name__ == '__main__':
    m = maze(10,15)
    m.CreateMaze()

    path, start = aStar(m)

    a = agent(m, x=start[0], y=start[1], footprints=True)
    m.tracePath({a:path})
    m.run()
