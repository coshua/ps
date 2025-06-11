class Solution:
    def romanToInt(self, s: str) -> int:
        # CD CM
        # IV IX
        # XL XC

        # X XX XXX XL 
        # L

        # process four representation
        st = []
        ans = 0
        for ch in s:
            if ch == 'D' and st and st[-1] == 'C':
                st.pop()
                ans += 400
            elif ch == 'M' and st and st[-1] == 'C':
                st.pop()
                ans += 900
            elif ch == 'C' and st and st[-1] == 'X':
                st.pop()
                ans += 90
            elif ch == 'L' and st and st[-1] == 'X':
                st.pop()
                ans += 40
            elif ch == 'X' and st and st[-1] == 'I':
                st.pop()
                ans += 9
            elif ch == 'V' and st and st[-1] == 'I':
                st.pop()
                ans += 4
            else:
                st.append(ch)
        d = {'I': 1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        for ch in st:
            ans += d[ch]
        return ans