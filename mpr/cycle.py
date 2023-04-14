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
# Create a graph
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Check if the graph has a cycle
if graph.has_cycle():
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")
