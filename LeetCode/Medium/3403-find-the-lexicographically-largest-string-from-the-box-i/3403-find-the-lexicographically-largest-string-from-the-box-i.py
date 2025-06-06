class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        ans = ""
        lo, hi = 0, len(word) - numFriends + 1

        if numFriends == 1:
            return word
        while lo < len(word):
            ans = max(ans, word[lo:hi])
            lo += 1
            hi = min(hi + 1, len(word))
        
        return ans