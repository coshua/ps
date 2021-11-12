from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for i in range(numCourses)]
        cnt_enter = [0 for i in range(numCourses)]

        for post, pre in prerequisites:
            cnt_enter[post] += 1
            graph[pre].append(post)
        
        q = deque()

        for i in range(numCourses):
            if cnt_enter[i] == 0:
                q.append(i)
        
        ans = []
        while (q):
            course = q.popleft()
            ans.append(course)
            for nxt in graph[course]:
                cnt_enter[nxt] -= 1
                if cnt_enter[nxt] == 0:
                    q.append(nxt)

        if len(ans) == numCourses:
            return ans
        else:
            return []
if __name__ == "__main__":
    solution = Solution()
    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))