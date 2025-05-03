class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        lc, ld, rc, rd = 0, 0, 0, 0
        p = 0
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                rc += 1
                rd += i
        
        while p < len(boxes):
            ans[p] = ld + rd
            if boxes[p] == '1':
                lc += 1
                rc -= 1
            rd -= rc
            ld += lc
            p += 1
        
        return ans

if __name__  == "__main__":
    sol = Solution()
    print(sol.minOperations("001011"))