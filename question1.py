import heapq
def dijkstra(graph, start, end):
    # Initialize distances 
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    # Priority queue to store nodes 
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        #neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            #update distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    #shortest path from start to end
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    return path

def find_shortest_route(nodes, edges, start_node, end_node):
    #graph from the list of edges
    graph = {node: {} for node in nodes}
    for edge in edges:
        graph[edge['from']][edge['to']] = edge['weight']
        graph[edge['to']][edge['from']] = edge['weight'] 
    shortest_route = dijkstra(graph, start_node, end_node)
    return shortest_route
#test1
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges = [
    {"from": "A", "to": "B", "weight": 1},
    {"from": "B", "to": "C", "weight": 3},
    {"from": "B", "to": "E", "weight": 3.5},
    {"from": "C", "to": "E", "weight": 4},
    {"from": "C", "to": "D", "weight": 2.5},
    {"from": "D", "to": "G", "weight": 2.5},
    {"from": "G", "to": "F", "weight": 3.5},
    {"from": "E", "to": "F", "weight": 2},
    {"from": "F", "to": "H", "weight": 2.5},
    {"from": "H", "to": "I", "weight": 1}
]

# Find shortest route from C to F
start_node = 'C'
end_node = 'F'
shortest_route = find_shortest_route(nodes, edges, start_node, end_node)
print(shortest_route)
