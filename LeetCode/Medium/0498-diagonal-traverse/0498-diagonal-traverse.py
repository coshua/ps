class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        rsz, csz = len(mat), len(mat[0])
        def traverse(r, c):
            local = []
            while 0 <= r < rsz and 0 <= c < csz:
                local.append(mat[r][c])
                r += 1
                c -= 1
            
            return local
        
        d=0
        r=c=0
        while r < rsz and c < csz:
            tmp = traverse(r,c)
            if d == 0:
                ans += tmp[::-1]
            else:
                ans += tmp
            d ^= 1

            if c == csz-1:
                r += 1
            else:
                c += 1
        return ans