class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inc = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[a].append(b)
            inc[b] += 1
        
        q = [i for i, v in enumerate(inc) if v == 0]
        numCourses -= len(q)

        while q:
            c = q.pop()
            for nxt in g[c]:
                inc[nxt] -= 1
                if inc[nxt] == 0:
                    q.append(nxt)
                    numCourses -= 1
                    
        return numCourses == 0