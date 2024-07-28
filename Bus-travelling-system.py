import heapq
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 5},
    'D': {'B': 1, 'C': 5}
}

def dij(graph, start):
    queue = [(0, start)]
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0
    previous_nodes = {}
    for vertex in graph:
        previous_nodes[vertex] = None
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))
    return distances, previous_nodes

def main(graph, start, end):
    distances, previous_nodes = dij(graph, start)
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]
    path = path[::-1]
    return path, distances[end]

path, cost = main(graph, 'A', 'B')
print(path)
print(f"cost = {cost}")