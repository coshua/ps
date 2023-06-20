import heapq as hq


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # [height, endpoint]
        heightq = [[0, 2**31]]
        buildings.append([2**31, 2**31, 0])
        contours = []

        for s, e, h in buildings:
            while s > heightq[0][1]:
                cur = hq.heappop(heightq)
                if cur[1] > contours[-1][0]:
                    while cur[1] > heightq[0][1]:
                        hq.heappop(heightq)
                    if -heightq[0][0] != contours[-1][1]:
                        contours.append([cur[1], -heightq[0][0]])

            if h > -heightq[0][0]:
                contours.append([s, h])
            hq.heappush(heightq, [-h, e])

        return contours


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSkyline([[0, 2, 3], [2, 5, 3]]))
