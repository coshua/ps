class Solution:
    def findStrobogrammatic(self, nn: int) -> List[str]:
        ans = []

        mp = {"1": "1", "6":"9", "9":"6", "8":"8", "0":"0"}
        
        def helper(n):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            
            sub = helper(n-2)
            local = []
            for key in mp:
                if n == nn and key == "0":
                    continue
                for elem in sub:
                    local.append(key + elem + mp[key])
            return local
        return helper(nn)
