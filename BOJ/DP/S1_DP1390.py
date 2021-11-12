n = int(input())

dp_no = [0] * ( n + 1 )
dp_left = [0] * (n+1)
dp_right = [0]*(n+1)

dp_no[0] = 1

for i in range(1, n + 1):
    dp_no[i] = (dp_left[i - 1] + dp_right[i - 1] + dp_no[i - 1]) % 9901
    dp_left[i] = (dp_no[i - 1] + dp_right[i - 1]) % 9901
    dp_right[i] = (dp_no[i - 1] + dp_left[i - 1]) % 9901

print((dp_no[n] + dp_left[n] + dp_right[n]) % 9901)
