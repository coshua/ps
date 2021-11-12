import math
import sys 
input = sys.stdin.readline
list(map(int, input().split()))
def calc(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)) * 0.5

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

N = int(input())
triangle = [()] * (N - 2)

