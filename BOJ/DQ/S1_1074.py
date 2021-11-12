N, r, c = map(int, input().split())

def dq(n, r, c, acc):
    if n == 1:
        return acc + r * 2 + c + 1
    
    section_amount = pow(pow(2, n - 1), 2)

    if r > pow(2, n - 1) - 1 and c > pow(2, n - 1) - 1:
        return dq(n - 1, r - pow(2, n - 1), c - pow(2, n - 1), acc + section_amount * 3)
    elif r > pow(2, n - 1) - 1:
        return dq(n - 1, r - pow(2, n - 1), c, acc + section_amount * 2)
    elif c > pow(2, n - 1) - 1:
        return dq(n - 1, r, c - pow(2, n - 1), acc + section_amount)
    else:
        return dq(n - 1, r, c, acc)
print(dq(N, r, c, -1))