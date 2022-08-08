import heapq
#한 정점에서 다른 모든 정점으로의 최단거리 구하기
def dijkstra(graph, start):
    q = [(0, start)]
    distance = [float('inf')] * len(graph)
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for nxt_d, nxt_v in graph[node]:
            cost = dist + nxt_d
            if cost < distance[nxt_v]:
                distance[nxt_v] = cost
                heapq.heappush(q, (cost, nxt_v))
    
    return distance
