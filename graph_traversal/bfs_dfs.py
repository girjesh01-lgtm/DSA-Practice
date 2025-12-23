from collections import deque

# Sample graph representation as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

graph = {
    "Alice": ["Bob", "Claire", "Frank"],
    "Bob": ["Alice", "Dennis", "Eve"],
    "Claire": ["Alice", "Frank"],
    "Dennis": ["Bob"],
    "Eve": ["Bob"],
    "Frank": ["Alice", "Claire"],
}

# ----------------------------------
# Breath-First-Search (BFS)
# ----------------------------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


# ----------------------------------
# Depth-First-Search (DFS)
# ----------------------------------
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("BFS traversal:")
#bfs(graph, 'A')  # Output: A B C D E F
bfs(graph, "Alice")
print("\n\nDFS traversal:")
#print("\nDFS traversal:")
dfs(graph, 'Alice')  # Output: A B D E F C

