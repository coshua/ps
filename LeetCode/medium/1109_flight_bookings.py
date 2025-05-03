import heapq
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ans = [0] * (n + 1)
        pointer = 1
        subt = []
        bookings.sort(key = lambda x : x[0])
        acc = 0
        for booking in bookings:
            heapq.heappush(subt, (booking[1] + 1, booking[2]))

            while pointer < booking[0]:
                while subt and pointer >= subt[0][0]:
                    acc -= heapq.heappop(subt)[1]
                ans[pointer] = acc
                pointer += 1
            
            acc += booking[2]
    
        while pointer <= n:
            while subt and pointer >= subt[0][0]:
                acc -= heapq.heappop(subt)[1]
            ans[pointer] = acc
            pointer += 1
        
        return ans[1:]