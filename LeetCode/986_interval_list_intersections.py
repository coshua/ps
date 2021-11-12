class Solution:
    def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
        pointer = [0, 0]
        lst = [firstlist, secondlist]
        ans = []
        if len(firstlist) == 0 or len(secondlist) == 0:
            return ans
        
        # we assume lane that has opening block is called 0.
        open = 0
        while pointer[0] < len(firstlist) and pointer[1] < len(secondlist):
            if lst[open][pointer[open]][0] > lst[open ^ 1][pointer[open ^ 1]][0]:
                open ^= 1

            if lst[open ^ 1][pointer[open ^ 1]][0] > lst[open][pointer[open]][1]:
                pointer[open] += 1
            
            elif lst[open ^ 1][pointer[open ^ 1]][1] < lst[open][pointer[open]][1]:
                ans.append(lst[open ^ 1][pointer[open ^ 1]])
                pointer[open ^ 1] += 1
            
            elif lst[open ^ 1][pointer[open ^ 1]][1] == lst[open][pointer[open]][1]:
                ans.append(lst[open ^ 1][pointer[open ^ 1]])
                pointer[open] += 1
                pointer[open ^ 1] += 1
            
            else:
                ans.append([lst[open ^ 1][pointer[open ^ 1]][0], lst[open][pointer[open]][1]])
                pointer[open] += 1
         
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
        