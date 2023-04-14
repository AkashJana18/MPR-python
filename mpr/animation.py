import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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

        # yield current state of visited and rec_stack arrays
        yield visited.copy(), rec_stack.copy()

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                yield from self.has_cycle_util(neighbour, visited, rec_stack)
                if any(rec_stack):  # if any cycle found in child, break
                    break
            elif rec_stack[neighbour]:
                rec_stack[v] = False  # set the last node to False in rec_stack
                yield visited.copy(), rec_stack.copy()
                yield True  # yield that a cycle is detected

        rec_stack[v] = False
        yield visited.copy(), rec_stack.copy()

    def has_cycle(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                yield from self.has_cycle_util(node, visited, rec_stack)

# Create a graph
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_title('DFS Algorithm for Cycle Detection')
ax.set_xlabel('Vertices')
ax.set_ylabel('Visited/Recursion Stack')

# Create the plot lines for visited and recursion stack
visited_line, = ax.plot([], [], 'bo-', label='Visited')
rec_stack_line, = ax.plot([], [], 'ro-', label='Recursion Stack')
ax.legend()

# Initialize the visited and recursion stack arrays
visited = [False] * graph.vertices
rec_stack = [False] * graph.vertices

# Initialize the cycle detection text
cycle_detected_text = ax.text(0.5, 0.9, '', transform=ax.transAxes, ha='center')

def update(i):
    global visited, rec_stack
    if isinstance(i, bool):  # if a cycle is detected
        cycle_detected_text.set_text('Cycle detected!')
        visited, rec_stack = [False] * graph.vertices, [False] * graph.vertices
        return visited_line, rec_stack_line, cycle_detected_text

    visited, rec_stack = i[0], i[1]
    visited_line.set_data(range(graph.vertices), visited)
    rec_stack_line.set_data(range(graph.vertices), rec_stack)
    cycle_detected_text.set_text('')

    return visited_line, rec_stack_line, cycle_detected_text

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=graph.has_cycle, blit=True, repeat=False)

# Show the plot and start the animation
plt.show()
