class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pnt = 0
        if not n:
            return True
        while pnt < len(flowerbed):
            prev = flowerbed[pnt-1] if pnt > 0 else 0
            nxt = flowerbed[pnt+1] if pnt < len(flowerbed) - 1 else 0
            if prev + nxt + flowerbed[pnt] == 0:
                n -= 1
                flowerbed[pnt] = 1
                if n == 0:
                    return True
            pnt += 1
        return False