import sys 
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

visited = set()
neighbor = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    neighbor[u].append((v, w))
def dijkstra(start):
    dist = [float("INF")] * (V + 1)
    dist[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (curdist, curvertex) = pq.get()

        if curvertex not in visited:
            visited.add(curvertex)

            for nextvertex, weight in neighbor[curvertex]:
                if nextvertex not in visited:
                    oldcost = dist[nextvertex]
                    newcost = dist[curvertex] + weight
                    if newcost < oldcost:
                        pq.put((newcost, nextvertex))
                        dist[nextvertex] = newcost
    
    return dist

ans = dijkstra(start)
for i in range(1, V + 1):
    if ans[i] == float('inf'):
        print("INF")
    else:
        print(ans[i])
