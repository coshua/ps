class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch.isalpha():
                st.append(ch.lower())
            elif ch.isdigit():
                st.append(ch)
        
        lo, hi = 0, len(st)-1
        while lo < hi:
            if st[lo] != st[hi]:
                return False
            lo += 1
            hi -= 1
        return True