class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        def findCoupleIdx(n, lst):
            target = n
            if n % 2 == 0:
                target += 1
            else:
                target -= 1
            return lst.index(target)

        swaps = 0
        for i in range(0, len(row), 2):
            partneridx = findCoupleIdx(row[i], row)
            anotherCoupleFstIdx = partneridx
            if partneridx % 2 == 0:
                anotherCoupleFstIdx += 1
            else:
                anotherCoupleFstIdx -= 1

            anotherCoupleFstVal = row[anotherCoupleFstIdx]
            anotherCoupleSndVal = anotherCoupleFstVal
            if anotherCoupleFstVal % 2 == 0:
                anotherCoupleSndVal += 1
            else:
                anotherCoupleSndVal -= 1

            anotherCoupleSndIdx = findCoupleIdx(anotherCoupleSndVal, row)

            if anotherCoupleSndIdx == i:
                # it means a pair of couple holding hands at row[i] and row[i + 1]
                continue
            else:
                swaps += 1
                row[i + 1], row[partneridx] = row[partneridx], row[i + 1]
        return swaps


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSwapsCouples([10, 7, 4, 2, 3, 0, 9, 11, 1, 5, 6, 8]))
