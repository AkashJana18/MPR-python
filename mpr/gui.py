import tkinter as tk
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.has_cycle_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[v] = False
        return False

    def has_cycle(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                if self.has_cycle_util(node, visited, rec_stack):
                    return True

        return False

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.option_label = tk.Label(self.master, text="Choose an option:")
        self.option_label.pack(pady=10)

        self.cycle_directed_button = tk.Button(self.master, text="Detect cycle in directed graph", command=self.detect_cycle_directed)
        self.cycle_directed_button.pack()

        self.cycle_undirected_button = tk.Button(self.master, text="Detect cycle in undirected graph", command=self.detect_cycle_undirected)
        self.cycle_undirected_button.pack()

        self.shortest_path_button = tk.Button(self.master, text="Shortest path", command=self.shortest_path)
        self.shortest_path_button.pack()

        self.salesman_button = tk.Button(self.master, text=" Traveling Salesman Problem ", command=self.salesman_path)
        self.salesman_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=10)

    def detect_cycle_directed(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)
        graph.add_edge(3, 3)

        if graph.has_cycle():
            tk.messagebox.showinfo("Result", "The directed graph has a cycle.")
        else:
            tk.messagebox.showinfo("Result", "The directed graph does not have a cycle.")

    def detect_cycle_undirected(self):
        # Code for detecting cycle in an undirected graph
        tk.messagebox.showinfo("Result", "Cycle detection in undirected graph.")

    def shortest_path(self):
        # Code for finding the shortest path in a graph
        tk.messagebox.showinfo("Result", "Shortest path.")

    def salesman_path(self):
        # Code for finding the salesman's path in a graph
        tk.messagebox.showinfo("Result", "Salesman's path.")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
