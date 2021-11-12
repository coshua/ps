import sys
input = sys.stdin.readline

first_s = list(input().strip())
sec_s = list(input().strip())

max_len = 0

dp = [0] * (len(first_s))

for i in range(len(sec_s)):
    nxt = [0] * (len(first_s))
    for j in range(len(first_s)):
        if sec_s[i] == first_s[j]:
            if i == 0 or j == 0:
                nxt[j] = 1
            else:
                nxt[j] = dp[j - 1] + 1
            max_len = max(max_len, nxt[j])
    dp = nxt
print(max_len)