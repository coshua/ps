class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        d = set()
        ans = ""
        d.add(str1)
        for i in range(len(str1) // 2):
            if len(str1) % (i + 1) == 0:
                divisible = True
                for j in range(i, len(str1), i):
                    if str1[:i] != str1[j: i + j]:
                        divisible = False
                        break
                if divisible:
                    d.add(str1[:i])
        if str2 in d:
            return str2
        for i in range(len(str2) // 2):
            if len(str2) % (i + 1) == 0:
                divisible = True
                for j in range(i, len(str2), i):
                    if str2[:i] != str2[j: i + j]:
                        divisible = False
                        break
                if divisible and str2[:i] in d:
                    if len(str2[:i]) > len(ans):
                        ans = str2[:i]
        return ans
        
        

