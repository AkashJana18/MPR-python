import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Dijkstra's Algorithm")


start_node_label = tk.Label(window, text="Start Node:")
start_node_label.grid(row=0, column=0, sticky=tk.W)
start_node_entry = tk.Entry(window)
start_node_entry.grid(row=0, column=1)

end_node_label = tk.Label(window, text="End Node:")
end_node_label.grid(row=1, column=0, sticky=tk.W)
end_node_entry = tk.Entry(window)
end_node_entry.grid(row=1, column=1)


graph_label = tk.Label(window, text="Graph (Adjacency Matrix):")
graph_label.grid(row=2, column=0, sticky=tk.W)
graph_text = tk.Text(window, height=10, width=30)
graph_text.grid(row=2, column=1)


def dijkstra():
    start_node = start_node_entry.get()
    end_node = end_node_entry.get()
    graph = graph_text.get("1.0", tk.END)
    try:
       
        adjacency_matrix = [[int(cell) for cell in row.split()] for row in graph.split("\n")]
        num_nodes = len(adjacency_matrix)

       
        distance = [float('inf')] * num_nodes
        distance[int(start_node)] = 0
        visited = [False] * num_nodes

        
        for _ in range(num_nodes):
            min_distance = float('inf')
            min_node = None
            for node in range(num_nodes):
                if not visited[node] and distance[node] < min_distance:
                    min_distance = distance[node]
                    min_node = node
            if min_node is None:
                break
            visited[min_node] = True
            for neighbor in range(num_nodes):
                if (not visited[neighbor] and
                        adjacency_matrix[min_node][neighbor] > 0 and
                        distance[min_node] + adjacency_matrix[min_node][neighbor] < distance[neighbor]):
                    distance[neighbor] = distance[min_node] + adjacency_matrix[min_node][neighbor]

        
        messagebox.showinfo("Dijkstra's Algorithm", f"Shortest distance from node {start_node} to node {end_node}: {distance[int(end_node)]}")
    except:
        messagebox.showerror("Error", "Invalid input. Please check your input and try again.")


calculate_button = tk.Button(window, text="Calculate", command=dijkstra)
calculate_button.grid(row=3, column=0, columnspan=2)


window.mainloop()