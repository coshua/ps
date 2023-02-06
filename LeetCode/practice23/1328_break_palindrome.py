class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        minstr = palindrome
        for i in range(len(palindrome)):
            if len(palindrome) % 2 == 1 and i == len(palindrome) // 2:
                continue
            for j in range(25):
                n = ord(palindrome[i]) - ord('a')
                if j == n:
                    continue
                else:
                    sw = palindrome[:i] + chr(ord('a') + j) + palindrome[i + 1:]
                    if minstr == palindrome:
                        minstr = sw
                    else:
                        minstr = min (minstr, sw)
                    break
        if minstr == palindrome:
            return ""
        else:
            return minstr