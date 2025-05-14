class Solution:
    def compress(self, chars: List[str]) -> int:
        pnt = 0
        chars.append("-1")
        prev = chars[0]
        cnt = 1
        for i in range(1, len(chars)):
            cur = chars[i]
            if cur == prev:
                cnt += 1
            else:
                chars[pnt] = prev
                pnt += 1
                if cnt > 1:
                    str_cnt = str(cnt)
                    for str_ch in str_cnt:
                        chars[pnt] = str_ch
                        pnt += 1
                cnt = 1
                prev = cur
            
        return pnt