import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()

def check(s):
    if len(s) <= 2:
        return True
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return check(s[:len(s) // 2]) and check(s[-(len(s) // 2):])

if check(s):
    print("AKARAKA")
else:
    print("IPSELENTI")