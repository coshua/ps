class Solution:
    cnt = 0
    def numDecodings(self, s: str) -> int:
        def decodableWithTwo(s):
            if len(s) < 2:
                return False
            if s[0] == '0':
                return False
            if len(s) > 2 and s[2] == '0':
                return False
            if s[0] == '1':
                return True
            elif s[0] == '2':
                if '0' <= s[1] <= '6':
                    return True
            return False

        def decodableWithOne(s):
            if len(s) < 1:
                return False
            if s[0] == '0':
                return False
            return True

        def decode(s):
            if len(s) == 0:
                self.cnt += 1
                return
            if decodableWithTwo(s):
                decode(s[2:])
            if decodableWithOne(s):
                decode(s[1:])

        decode(s)
        return self.cnt
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("27"))
        