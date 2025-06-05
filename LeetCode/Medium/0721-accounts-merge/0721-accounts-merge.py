class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = defaultdict(list)

        for acc in accounts:
            name, emails = acc[0], acc[1:]
            for i in range(len(emails) - 1):
                pe, ne = emails[i], emails[i + 1]
                g[pe].append(ne)
                g[ne].append(pe)
        
        v = set()
        ans = []

        def dfs(email, path):
            for nxt in g[email]:
                if nxt not in v:
                    v.add(nxt)
                    path.append(nxt)
                    dfs(nxt, path)
        for acc in accounts:
            name, emails = acc[0], acc[1:]
            if emails[0] in v:
                continue
            path = [emails[0]]
            v.add(emails[0])
            dfs(emails[0], path)
            path.sort()
            ans.append([name] + path)
        return ans