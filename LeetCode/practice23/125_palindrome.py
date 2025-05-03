class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        for ch in s:
            n = ord(ch)
            if ord('A') <= n <= ord('Z'):
                st.append(ch.lower())
            elif ord('a') <= n <= ord('z') or ord('0') <= n <= ord('9'):
                st.append(ch)

        return st == st[::-1]