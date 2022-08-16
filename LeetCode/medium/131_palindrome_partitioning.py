class Solution:
    def partition(self, s):
        comb = []

        def isPalindrome(s):
            f = 0
            e = len(s) - 1
            while f < e:
                if s[f] != s[e]:
                    return False
                f += 1
                e -= 1
            return True

        def recurse(lst, s):
            if len(s) == 0:
                comb.append(lst)
                return
            
            for i in range(1, len(s) + 1):
                if isPalindrome(s[0:i]):
                    p = s[0:i]
                    tmp = lst[:]
                    tmp.append(p)
                    recurse(tmp, s[i:])
        recurse([], s)
        return comb

if __name__ == "__main__":
    solution = Solution()
    print(solution.partition("a"))