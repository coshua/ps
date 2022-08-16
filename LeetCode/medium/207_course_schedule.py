from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        enter_cnt = [0 for i in range(numCourses)]
        for pre, post in prerequisites:
            enter_cnt[post] += 1
            graph[pre].append(post)
        
        ln = numCourses
        q = deque()
        for i in range(ln):
            if enter_cnt[i] == 0:
                q.append(i)
        
        while(q):
            course = q.popleft()
            numCourses -= 1
            for i in graph[course]:
                enter_cnt[i] -= 1
                if enter_cnt[i] == 0:
                    q.append(i)
        
        return numCourses == 0
if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(2, [[1, 0], [0, 1]]))