class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = [] # minheap

        rsz, csz = len(matrix), len(matrix[0])
        for i in range(rsz):
            heapq.heappush(q, (matrix[i][0], i, 0))
        while q:
            v, r, c= heapq.heappop(q)
            k -= 1
            if k == 0:
                return v
            if c+1 < csz:
                heapq.heappush(q, (matrix[r][c+1], r, c+1))
        return -1
