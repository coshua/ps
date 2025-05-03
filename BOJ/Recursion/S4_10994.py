T = int(input())

m = [[' '] * (4 * T - 3) for i in range(4 * T - 3)]
def rec(n, id):
    if n == 1:
        m[id][id] = '*'
        return
    tid = id
    bid = 4 * T - 4 - id
    for i in range(4 * n - 3):
        m[tid][id + i] = '*'
        m[bid][id + i] = '*'
        m[id + i][tid] = '*'
        m[id + i][bid] = '*'
    rec(n - 1, id + 2)

rec(T, 0)
for i in range(4 * T - 3):
    print("".join(m[i])) 