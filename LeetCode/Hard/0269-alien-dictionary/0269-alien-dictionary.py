class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = [[] for _ in range(26)]
        pre_cnt = [0] * 26
        v = set()
        def process(pre, pro, g, cnt):
            idx = 0
            while idx < len(pre) and idx < len(pro) and pre[idx] == pro[idx]:
                idx += 1
            print(idx)
            if pre == pro:
                return True
            if idx >= len(pro):
                return False
            if idx >= len(pre):
                return True
            
            pre_idx = ord(pre[idx]) - ord('a')
            pro_idx = ord(pro[idx]) - ord('a')

            g[pre_idx].append(pro_idx)
            cnt[pro_idx] += 1
            return True
        for ch in words[0]:
            v.add(ch)
        for i in range(len(words) - 1):
            flag = process(words[i], words[i + 1], graph, pre_cnt)
            for c in words[i]:
                v.add(c)
            for c in words[i + 1]:
                v.add(c)
            if not flag:
                return ""
        print(graph)
        seq = ""
        q = []
        for i in range(26):
            if not pre_cnt[i] and chr(i + ord('a')) in v:
                q.append(i)
        while q:
            cur = q.pop()
            seq += chr(cur + ord('a'))
            for nxt in graph[cur]:
                pre_cnt[nxt] -= 1
                if pre_cnt[nxt] == 0:
                    q.append(nxt)
        if sum(pre_cnt) > 0:
            return ""
        return seq
