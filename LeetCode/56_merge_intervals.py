class Solution:
    def merge(self, intervals):
        v = [0] * 10001
        id = 1
        for s, e in intervals:
            if v[s] == 0 and v[e] == 0:
                for i in range(s, e + 1):
                    v[i] = id
                id += 1

            elif v[s] > 0 and v[e] == 0:
                merge_id = v[s]
                i = e
                while v[i] != merge_id:
                    v[i] = merge_id
                    i -= 1
            
            elif v[s] == 0 and v[e] > 0:
                merge_id = v[e]
                i = s
                while v[i] != merge_id:
                    v[i] = merge_id
                    i += 1
            
            elif v[s] > 0 and v[e] > 0 and v[s] != v[e]:
                merge_id = v[s]
                merged_id = v[e]
                i = e
                while v[i] != merge_id:
                    v[i] = merge_id
                    i -= 1
                i = e + 1
                while i < 10001 and v[i] == merged_id:
                    v[i] = merge_id
                    i += 1
        sections = list()
        cur = 0
        start = -1
        for i in range(0, 10001):
            if v[i] == 0 and cur == 0:
                continue

            elif v[i] > 0 and cur == 0:
                cur = v[i]
                start = i
            
            elif v[i] > 0 and v[i] == cur:
                continue

            elif v[i] != cur and cur > 0:
                sections.append([start, i - 1])
                start = -1
                if v[i] > 0:
                    start = i
                cur = v[i]
        if start > 0:
            sections.append([start, 10000])
        return sections
if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[5,7],[4,4],[2,3],[6,10],[9,12],[2,5],[7,10],[1,1],[0,4],[5,5],[7,11]]))