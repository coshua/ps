class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combs = []
        candidates.sort(reverse = True)
        def addingOneElement(acc, lst, idx):
            if acc == target:
                combs.append(lst)
            elif idx >= len(candidates):
                return
            else:
                while idx < len(candidates) and acc + candidates[idx] > target:
                    idx += 1
                for nxtidx in range(idx, len(candidates)):
                    nxtacc = acc + candidates[nxtidx]
                    nxtlst = lst[:]
                    nxtlst.append(candidates[nxtidx])
                    addingOneElement(nxtacc, nxtlst, nxtidx)
        addingOneElement(0, [], 0)
        return combs
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 7, 6], 7))  