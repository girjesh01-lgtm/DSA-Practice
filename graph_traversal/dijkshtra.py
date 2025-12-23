import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    print(dist)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)

        if cur_dist > dist[node]:
            continue

        for nei, weight in graph[node]:
            new_dist = cur_dist + weight
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(pq, (new_dist, nei))

    return dist


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 3)],
    'C': [('E', 1)],
    'D': [],
    'E': []
}


print(dijkstra(graph, 'A'))