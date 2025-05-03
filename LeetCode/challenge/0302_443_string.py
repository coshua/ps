class Solution:
    def compress(self, chars: list[str]) -> int:
        p = 0
        prev = None
        cnt = 0
        for ch in chars:
            if not prev:
                prev = ch
                cnt = 1
            elif prev != ch:
                chars[p] = prev
                p += 1
                if cnt > 1:
                    cnt = str(cnt)
                    for s in cnt:
                        chars[p] = s
                        p += 1
                prev = ch
                cnt = 1
            else:
                cnt += 1
        
        chars[p] = prev
        p += 1
        if cnt > 1:
            cnt = str(cnt)
            for s in cnt:
                chars[p] = s
                p += 1
        return p