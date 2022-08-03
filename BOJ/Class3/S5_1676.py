import math
import sys
input = sys.stdin.readline

T = int(input())

cnt_5 = 0
for i in range(T + 1):
    n = i
    while n % 5 == 0 and n > 0:
        n //= 5
        cnt_5 += 1

print(cnt_5)