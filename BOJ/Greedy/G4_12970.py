N, K = map(int, input().split())
n = N // 2 if N % 2 == 0 else N // 2 + 1
if (K > (N // 2) * n):
    print(-1)
else:
    s = "A" * n + "B" * (N // 2)
    s = list(s)
    pairs = (N // 2) * n
    b_index = (N // 2)
    moving_b = (N // 2)
    while pairs > K:
        s[moving_b - 1] = 'B'
        s[moving_b] = 'A'
        moving_b -= 1
        pairs -= 1
        if moving_b == 0 or s[moving_b - 1] == 'B':
            b_index += 1
            moving_b = b_index
    print(''.join(s))
