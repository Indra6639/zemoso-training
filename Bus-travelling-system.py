import heapq #Importing module for priority queue.

graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 5},
    'D': {'B': 1, 'C': 5},
    'E': {}
}#Initialization of bus travel route or nodes with weights.

def dijkstra(graph, start):
    if start not in graph:
        raise ValueError(f"Start vertex '{start}' not in the route.")
    queue = [(0, start)]
    distances = {}
    for vertex in graph:#Dictionary to store the shortest distance to each node.
        distances[vertex] = float('inf')
    distances[start] = 0#Initialize 0 to the starting node
    previous_nodes = {}
    for vertex in graph:#Dictionary to store the path of previous nodes.
        previous_nodes[vertex] = None
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)#Pick the vertex with smallest distance from the queue.
        if current_distance > distances[current_vertex]:
            continue #Ignore the vertex if its cost greater than the existing cost.
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight#Update the distance for each neighbour nodes
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))
    return distances, previous_nodes

def main(graph,start,end):
    try:
        distances, previous_nodes = dijkstra(graph, start)#Calling the dij function for cost and vertices.
        if distances[end] == float('inf'):
            return [], "vertex is not reachable"
        path = []
        current_vertex = end#Starting with the end of the path.
        while current_vertex is not None:
            path.append(current_vertex)#Adding all the nodes that involved in reverse order.
            current_vertex = previous_nodes[current_vertex]
        path.reverse()#Reverse the path
        return path, distances[end]
    except ValueError as e:
        return str(e),None

path, cost = main(graph,'A','E')#Calling the main function where E is tractable
print(path)
print(f"cost = {cost}")
print()

path, cost = main(graph,'X','D')#Calling the main function for non existing start vertex.
print(path)
print(f"cost = {cost}")
print()

path, cost = main(graph,'A','B')#Calling the main function.
print(path)
print(f"cost = {cost}")