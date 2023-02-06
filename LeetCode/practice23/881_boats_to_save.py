class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        cnt = 0
        pl, pr = 0, len(people) - 1
        while pl <= pr:
            if people[pl] + people[pr] <= limit:
                pl += 1
                pr -= 1
            elif people[pl] <= people[pr]:
                pr -=1
            else:
                pl += 1
            cnt += 1
        
        return cnt