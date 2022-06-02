class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ln = len(s)
        
        cnt_alphabets = [0] * 26
        
        for a in s:
            cnt_alphabets[ord(a) - ord('a')] += 1
        
        for a in t:
            cnt_alphabets[ord(a) - ord('a')] -= 1
        
        for num in cnt_alphabets:
            if num != 0:
                return False
            
        return True