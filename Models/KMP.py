#Knuth–Morris–Pratt for pattern searching, based on DP
#Given s, longest substring that is a prefix and also a suffix (excluding itself)

def kmp(s):
    dp = [0] * len(s)
    for i in range(1, len(s)):
        j = dp[i - 1]
        while j > 0 and s[j] != s[i]: j = dp[j - 1]
        if s[j] == s[i]: j += 1
        dp[i] = j
    
    print(dp)
    return s[:dp[-1]]

if __name__ == "__main__":
    s = "aabcdaab"
    kmp(s)