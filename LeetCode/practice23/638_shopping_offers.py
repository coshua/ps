class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        self.mincost = 0
        for i in range(len(price)):
            self.mincost += price[i] * needs[i]

        def backtrack(cost, occ, idx):
            curcost = cost
            for i in range(len(occ)):
                curcost += (needs[i] - occ[i]) * price[i]
            
            self.mincost = min(self.mincost, curcost)

            if occ == needs:
                return
                
            for i in range(idx, len(special)):
                nxtocc = occ[:]
                proceed = True
                for j in range(len(price)):
                    nxtocc[j] += special[i][j]
                    if nxtocc[j] > needs[j]:
                        proceed = False
                        break
                if proceed:
                    backtrack(cost + special[i][-1], nxtocc, i)


        backtrack(0, [0] * len(price), 0)
        return self.mincost

class Solution2:
    def shoppingOffers(self, price, special, needs):

        self.res = float('inf')
        self.dfs(needs,special,price,0,0)
        return self.res
        
    def dfs(self, needs, special, price, currentprice, specialindex):
        if needs == [ 0 for x in range(len(needs))]:
            self.res = min(self.res,currentprice)
            return
        for x in range(specialindex,len(special)):
            vaild = True
            for y in range(len(needs)):
                if needs[y] < special[x][y]:
                    vaild = False
                    break
            if vaild == True:
                nextneeds = [needs[a] - special[x][a] for a in range(len(needs))]
                self.dfs(nextneeds,special,price,currentprice+special[x][-1],x)
        for z in range(len(needs)):
            if needs[z] >= 1:
                currentprice += price[z]*needs[z]
        self.res = min(self.res,currentprice)

if __name__ == "__main__":
    solution = Solution2()
    print(solution.shoppingOffers([2, 2], [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]], [10, 10]))