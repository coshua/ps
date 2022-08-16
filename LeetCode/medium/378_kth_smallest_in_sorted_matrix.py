class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        self.cnt = 0

        def twoPointer(matrix, id):
            # p1 goes downward (id + i, id)
            p1 = id

            # p2 goes rightward (id, id + i + 1)
            p2 = id + 1

            while not (p1 == n and p2 == n):
                if p2 == n or matrix[p1][id] < matrix[id][p2]:
                    if self.cnt + 1 == k:
                        return matrix[p1][id]
                    p1 += 1
                else:
                    if self.cnt + 1 == k:
                        return matrix[id][p2]
                    p2 += 1
                self.cnt += 1
        
        for i in range(n):
            ans = twoPointer(matrix, i)
            if ans != None:
                return ans
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([[-5]], 1))