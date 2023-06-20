import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coords = []
for _ in range(N):
    coords.append(list(map(int, input().split())))

coords.sort()
contained = [0] * (K + 1)
minwidth = float('inf')
lo, hi = 0, 0
unique = 0

while hi < len(coords) and unique < K:
    contained[coords[hi][2]] += 1
    if contained[coords[hi][2]] == 1:
        unique += 1
    hi += 1
    
    while unique == K:
        print(lo, hi - 1, "width")
        minwidth = min(minwidth, coords[hi - 1][0] - coords[lo][0])
        contained[coords[lo][2]] -= 1
        if contained[coords[lo][2]] == 0:
            unique -= 1
        lo += 1

coords.sort(key = lambda x: x[1])
minheight = float('inf')
lo, hi, unique = 0, 0, 0
contained = [0] * (K + 1)
while hi < len(coords) and unique < K:
    contained[coords[hi][2]] += 1
    if contained[coords[hi][2]] == 1:
        unique += 1
    hi += 1
    
    while unique == K:
        print(lo, hi)
        minheight = min(minheight, coords[hi - 1][1] - coords[lo][1])
        contained[coords[lo][2]] -= 1
        if contained[coords[lo][2]] == 0:
            unique -= 1
        lo += 1

print(minwidth, minheight)

