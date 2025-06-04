# 👥 Ranked Friend Recommender with BFS Animation

This Python application is an interactive friend recommendation system that visualizes a social network graph and provides **ranked friend suggestions** using **Breadth-First Search (BFS)**. The GUI is built with **Tkinter**, and the graph is visualized with **NetworkX** and **Matplotlib**.

---

## 🎯 Features

* Clickable user nodes in a graph to trigger BFS
* Animated BFS traversal up to depth 2
* Friend suggestions based on mutual connections
* Visual representation of the search and ranking

---

## 📁 File Structure

```
├── main.py               # Main application script
├── users.csv             # List of user names
├── friendships.csv       # User-to-user friendships
└── README.md             # Project documentation
```

---

## 🧠 How It Works

1. **Graph Building**: Loads users and friendships from CSV files.
2. **Graph Display**: Nodes and edges are displayed using NetworkX.
3. **User Click**: Click on a node to start BFS from that user.
4. **BFS Traversal**:

   * Depth 1: Direct friends (colored orange)
   * Depth 2: Friends of friends (colored red)
   * Other nodes: Grey
5. **Recommendation**: Ranks depth-2 users by number of mutual friends and displays them in a list.

---

## 📄 Data Format

### users.csv

```csv
name
Alice
Bob
Charlie
```

### friendships.csv

```csv
user1,user2
Alice,Bob
Bob,Charlie
Alice,Charlie
```

---

## 🖥️ Installation & Usage

### Requirements

* Python 3.x
* pandas
* matplotlib
* networkx
* tkinter (comes with Python)

### Installation

```bash
pip install pandas matplotlib networkx
```

### Run the App

```bash
python main.py
```

Then click on any node in the graph to get friend suggestions.

---

## ✨ Customization

* You can modify `users.csv` and `friendships.csv` to reflect your own social network data.
* Adjust the BFS depth or modify the `animate_bfs_ranked()` function for different logic or visual styles.

---

## 🧑‍💻 Author

Developed by \[Your Name]. Contributions and feedback are welcome!

---

## 📜 License

This project is licensed under the MIT License.

---

## 📸 Demo

> *(Optional)* Add a screenshot or a GIF of the application in action for better understanding.
