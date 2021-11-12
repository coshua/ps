R, C = map(int, input().split())

def solution(r, c):
    if r == 1:
        return 1
    if r == 2:
        if c <= 7:
            return (c - 1) // 2 + 1
        else:
            return 4
    else:
        if c <= 4:
            return c
        elif c <= 6:
            return 4
        else:
            return c - 2
print(solution(R, C))

        