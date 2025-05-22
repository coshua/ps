class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        lst = re.split(r'[^a-zA-Z]+', paragraph)
        lst = [w for w in lst if w]
        banset = set(banned)
        max_cnt = 0
        ans = ""

        wcnt = defaultdict(int)

        for wd in lst:
            sz = len(wd)
            lo = 0 
            hi = sz - 1
            while not wd[lo].isalpha():
                lo += 1
            while not wd[hi].isalpha():
                hi -= 1
            processed = wd[lo:hi+1].lower()
            if processed in banset:
                continue
            wcnt[processed] += 1
            if wcnt[processed] > max_cnt:
                max_cnt = wcnt[processed]
                ans = processed
        
        return ans