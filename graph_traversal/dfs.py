def dfs(graph, node, visited=None):
    print(node)
    if node not in visited:
        visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor, visited)





graph = {
    "Alice": ["Bob", "Claire", "Frank"],
    "Bob": ["Alice", "Dennis", "Eve"],
    "Claire": ["Alice", "Frank"],
    "Dennis": ["Bob"],
    "Eve": ["Bob"],
    "Frank": ["Alice", "Claire"],
}

dfs(graph, "Alice", set())