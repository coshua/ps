from collections import deque
from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        graph = [[] for _ in range(len(source))]
        visited = set()
        dist = 0

        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(len(source)):
            q = deque([i])
            subset = defaultdict(int)
            lst = []
            while q:
                id = q.popleft()
                if id in visited:
                    continue
                subset[source[id]] += 1
                lst.append(id)
                visited.add(id)
                for nxt_id in graph[id]:
                    if nxt_id not in visited:
                        q.append(nxt_id)
            subtract = 0
            for ele in lst:
                if subset[target[ele]] > 0:
                    subtract += 1
                    subset[target[ele]] -= 1
            dist += len(lst) - subtract
        return dist