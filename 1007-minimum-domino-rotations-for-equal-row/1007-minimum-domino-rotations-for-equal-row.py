class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float('inf')
        for fig in range(1, 7):
            swap_top, swap_bot = 0, 0
            for i in range (len(tops)):
                if tops[i] != fig and bottoms[i] != fig:
                    swap_top = float('inf')
                    swap_bot = float('inf')
                    break
                if tops[i] != fig and bottoms[i] == fig:
                    swap_top += 1
                if tops[i] == fig and bottoms[i] != fig:
                    swap_bot += 1
            ans = min(min(swap_top, swap_bot), ans)
        
        return -1 if ans == float('inf') else ans