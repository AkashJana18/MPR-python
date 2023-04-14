import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        (dist, node) = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_distance = dist + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distances

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'D': 1}
}

start = 'A'
distances = dijkstra(graph, start)
print(distances)
