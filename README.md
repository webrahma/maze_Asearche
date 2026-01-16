# A* Pathfinding Algorithm Visualizer 🚀

A Python-based implementation of the **A* (A-Star) Search Algorithm**, one of the most popular techniques used in pathfinding and graph traversals.

## 📌 About the Project
This project visualizes how the A* algorithm finds the shortest path between a start node and an end node while avoiding obstacles. It uses a **heuristic function** to optimize the search process.

### 🧠 How A* Works
The algorithm makes decisions based on the formula:
$$f(n) = g(n) + h(n)$$

* **$g(n)$**: The actual cost from the start node to the current node $n$.
* **$h(n)$**: The estimated (heuristic) cost from node $n$ to the goal (e.g., Euclidean or Manhattan distance).
* **$f(n)$**: The total estimated cost of the path through node $n$.



## ✨ Features
* **Interactive Grid:** Create obstacles (walls) by clicking on the grid.
* **Real-time Visualization:** Watch the algorithm explore nodes in real-time.
* **Optimized Path:** Displays the final shortest path in a distinct color.
* **Customizable Heuristics:** Supports Manhattan and Euclidean distances.

## 🛠️ Built With
* **Python**
* **Pygame** (or mention whatever library you used for GUI/Visualization)

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. You may also need to install dependencies:
```bash
pip install pygame
