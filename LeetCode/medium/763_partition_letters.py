class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        removedChar = set()
        result = []

        def findlastindex(ch, s):
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ch:
                    return i
        
        def findsubset(i, s):
            end = findlastindex(s[i], s)
            removedChar.add(s[i])
            idx = i + 1
            while idx < end:
                if s[idx] not in removedChar:
                    end = max(end, findlastindex(s[idx], s))
                    removedChar.add(s[idx])
                idx += 1
            return end - i + 1
        
        for i in range(len(s)):
            if s[i] not in removedChar:
                result.append(findsubset(i, s))
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels("eccbbbbdec"))


        