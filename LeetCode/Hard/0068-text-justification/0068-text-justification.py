class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur = []
        chsz = 0
        ans = []
        for w in words:
            if chsz + len(cur) + len(w) > maxWidth:
                sp = maxWidth - chsz
                tmp = []
                if len(cur) == 1:
                    tmp.append(cur[0])
                    tmp.append(" "*sp)
                else:
                    each_sp = sp // (len(cur)-1)
                    rem = sp % (len(cur)-1)
                    for e in cur:
                        if tmp:
                            tmp.append(" "*each_sp) if rem <= 0 else tmp.append(" "*(each_sp+1))
                            rem -=1
                        tmp.append(e)
                ans.append(''.join(tmp))
                cur.clear()
                chsz = 0
            cur.append(w)
            chsz += len(w)
        tmp = ' '.join(cur)
        ans.append(tmp+' '*(maxWidth-len(tmp)))
        return ans