import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global max_words
    if cnt == K - 5:
        temp = 0
        for word in m:
            for i in word:
                if not learn[ord(i)-ord('a')]:
                    break
            else:
                temp += 1
        max_words = max(temp, max_words)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

if __name__ == '__main__':
    N, K = map(int, input().split())
    m = [set(input().strip()) for _ in range(N)]

    max_words = 0

    if K < 5 or K == 26:
        print(0 if K < 5 else N)
        sys.exit(0)
    learn = [False] * 26
    for c in ('a', 'n', 't', 'i', 'c'):
        learn[ord(c) - ord('a')] = True
    dfs(0, 0)

    print(max_words)