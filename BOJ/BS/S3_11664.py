import math
ax, ay, az, bx, by, bz, cx, cy, cz = list(map(int, input().split()))

dist = 10000000

def calcDist(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))
for i in range(10000):
    mx = abs(ax + bx) / 2
    my = abs(ay + by) / 2
    mz = abs(az + bz) / 2

    md = calcDist(cx, cy, cz, mx, my, mz)
    ad = calcDist(cx, cy, cz, ax, ay, az)
    bd = calcDist(cx, cy, cz, bx, by, bz)
    if (abs(md - dist) <= 0.00000000001):
        break
    dist = min(md, dist)
    if (ad < bd):
        bx = mx
        by = my
        bz = mz
    else:
        ax = mx
        ay = my
        az = mz
print(dist)