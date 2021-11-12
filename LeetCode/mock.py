class Solution:
    def customSortString(self, order: str, s: str) -> str:
        numCount = [0] * 26
        for ch in s:
            numCount[ord(ch) - ord('a')] += 1
        
        ans = ""

        for ch in order:
            ans += ch * numCount[ord(ch) - ord('a')]
            numCount[ord(ch) - ord('a')] = 0
        
        for i in range(26):
            if numCount[i] > 0:
                ans += numCount[i] * chr(i + ord('a'))
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcccd"))