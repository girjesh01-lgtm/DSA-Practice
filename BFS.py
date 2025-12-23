from collections import deque

def bfs_shortest_path(graph, start):
    queue = deque(start)
    distance = {start: 0}

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in distance:
                distance[nei] = distance[node] + 1
                queue.append(nei)

    return distance






graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

path = bfs_shortest_path(graph, 'A')
print(path)