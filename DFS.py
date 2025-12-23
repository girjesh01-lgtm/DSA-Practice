def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        print("node", node)
        print("visited", visited)
        print("stack", stack)
        if node in stack:
            return True
        if node in visited:
            print("---------------------in visited---------------------------------")
            print("node", node)
            print("visited", visited)
            print("stack", stack)
            return False

        visited.add(node)
        stack.add(node)

        for nei in graph[node]:
            if dfs(nei):
                return True

        stack.remove(node)
        return False

    for node in graph:
        #print('node', node)
        if dfs(node):
            return True

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

directed_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

#path = has_cycle(graph)
#print(path)
#print("---------------------------------------------------------------------------------------")
#print()
#print()
result = has_cycle(directed_graph)
print(result)


