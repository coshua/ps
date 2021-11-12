import sys
input = sys.stdin.readline
# a = list(map(int, input().strip()))

a = 0b1000
b = a >> 2
print(a, b)
c = format(10**16, 'b')
print(len(str(c)))
print(-1 == False)