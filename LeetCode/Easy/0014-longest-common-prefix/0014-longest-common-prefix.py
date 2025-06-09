class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        pnt = 0
        sz = len(strs)
        while True:
            if pnt >= len(strs[0]):
                return ''.join(ans)
            ch = strs[0][pnt]
            for i in range(1, sz):
                if pnt >= len(strs[i]) or strs[i][pnt] != ch:
                    return ''.join(ans)
            ans.append(ch)
            pnt += 1
        
        return ''.join(ans)