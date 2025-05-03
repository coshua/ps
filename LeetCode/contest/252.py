class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        cnt = 12
        cnt_side = 5
        side = 2
        while cnt < neededApples:
            cnt += (cnt_side + side + 1 + side + 2) * 4
            cnt_side = cnt_side + side + 1 + (side + 2) * 2
            side += 2
        return side * 4
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumPerimeter(1000000000))