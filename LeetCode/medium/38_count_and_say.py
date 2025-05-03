class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        toread = self.countAndSay(n - 1)
        ans = ""
        temp = toread[0]
        cnt = 1
        for i in range(1, len(toread)):
            if toread[i] == temp:
                cnt += 1
            else:
                ans += str(cnt) + temp
                temp = toread[i]
                cnt = 1
        ans += str(cnt) + temp
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(4))