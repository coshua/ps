class Solution:
    def smallestNumber(self, pattern: str) -> str:
        global ans
        ans = float('inf')
        used = [0] * 10
        def backtrack(arr, used):
            global ans
            if len(arr) == len(pattern) + 1:
                res = "".join(map(str, arr))
                ans = min(ans, int(res))
                return

            idx = arr[-1]
            if pattern[len(arr) - 1] == 'I':
                for i in range(idx + 1, 10):
                    if not used[i]:
                        used[i] = 1
                        nxtarr = arr[:]
                        nxtarr.append(i)
                        backtrack(nxtarr, used)
                        used[i] = 0
            else:
                for i in range(1, idx):
                    if not used[i]:
                        used[i] = 1
                        nxtarr = arr[:]
                        nxtarr.append(i)
                        backtrack(nxtarr, used)
                        used[i] = 0
        
        for i in range(1, 10):
            used[i] = 1
            backtrack([i], used)
            used[i] = 0
        
        return str(ans)
                
