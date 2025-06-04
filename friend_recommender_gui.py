
import csv
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque, defaultdict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import time

def load_users(filename):
    return set(pd.read_csv(filename)['name'])

def load_friendships(filename, users):
    graph = defaultdict(list)
    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        u1, u2 = row['user1'], row['user2']
        if u1 in users and u2 in users:
            graph[u1].append(u2)
            graph[u2].append(u1)
    return graph

class FriendRecommenderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ranked Friend Recommender with BFS Animation")

        self.users = load_users("users.csv")
        self.graph = load_friendships("friendships.csv", self.users)

        self.G = nx.Graph()
        for user, friends in self.graph.items():
            for friend in friends:
                self.G.add_edge(user, friend)

        self.pos = nx.spring_layout(self.G, seed=42)
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()
        self.canvas.mpl_connect("button_press_event", self.on_click)

        self.label = ttk.Label(master, text="Click a user node to get ranked friend recommendations", font=('Arial', 14))
        self.label.pack(pady=10)

        self.recommendations_box = tk.Listbox(master, height=10, width=50)
        self.recommendations_box.pack(pady=5)

        self.draw_graph()

    def draw_graph(self, node_colors=None):
        self.ax.clear()
        if not node_colors:
            node_colors = ['skyblue'] * len(self.G.nodes)
        nx.draw_networkx(self.G, self.pos, ax=self.ax,
                         with_labels=True, node_color=node_colors, edge_color='gray',
                         node_size=800, font_size=10)
        self.ax.set_title("Social Network Graph (Click on a user)", fontsize=16)
        self.ax.axis('off')
        self.canvas.draw()

    def on_click(self, event):
        if event.inaxes == self.ax:
            for node, (x, y) in self.pos.items():
                radius = 0.05
                if (abs(x - event.xdata) < radius) and (abs(y - event.ydata) < radius):
                    self.animate_bfs_ranked(node)
                    break

    def animate_bfs_ranked(self, user):
        visited = set()
        queue = deque([(user, 0)])
        max_depth = 2
        mutual_friend_count = defaultdict(int)

        self.label.config(text=f"Ranked BFS Recommendations from {user}")
        self.recommendations_box.delete(0, tk.END)

        node_colors_map = {n: 'lightgray' for n in self.G.nodes}
        node_colors_map[user] = 'green'
        visited.add(user)
        user_friends = set(self.graph[user])

        while queue:
            current_user, depth = queue.popleft()

            if depth == 1:
                node_colors_map[current_user] = 'orange'
            elif depth == 2:
                node_colors_map[current_user] = 'red'
                mutuals = user_friends.intersection(self.graph[current_user])
                mutual_friend_count[current_user] = len(mutuals)

            color_list = [node_colors_map[n] for n in self.G.nodes]
            self.draw_graph(color_list)
            self.ax.set_title(f"Visiting: {current_user} (Depth {depth})", fontsize=14)
            self.canvas.draw()
            self.master.update()
            time.sleep(0.8)

            if depth < max_depth:
                for neighbor in self.graph.get(current_user, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))

        sorted_recs = sorted(mutual_friend_count.items(), key=lambda x: -x[1])
        if sorted_recs:
            for name, score in sorted_recs:
                self.recommendations_box.insert(tk.END, f"{name} (mutual friends: {score})")
        else:
            self.recommendations_box.insert(tk.END, "No ranked recommendations found")

def run_app():
    root = tk.Tk()
    app = FriendRecommenderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
