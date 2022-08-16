class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a)- len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        
        sum = [0] * (len(a) + 1)

        for i in range(1, len(a) + 1):
            if a[-i] == "1" and b[-i] == "1":
                sum[-i] = 2
            elif a[-i] == "1" or b[-i] == "1":
                sum[-i] = 1
        
        for i in range (1, len(a) + 1):
            if sum[-i] >= 2:
                sum[-i] -= 2
                sum[-i - 1] += 1
        if sum[0] == 0:
            sum = sum[1:]
        return "".join(map(str, sum))

if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("10111", "10"))
            