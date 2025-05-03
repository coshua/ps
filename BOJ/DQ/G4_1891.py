ln, D = list(input().strip().split())

dx, dy = list(map(int, input().split()))

def quadrant(n, d):
    if d == '2':
        return 0, 0
    elif d == '1':
        return 0, pow(2, n)
    elif d == '3':
        return pow(2, n), 0
    elif d == '4':
        return pow(2, n), pow(2, n)
    else:
        return 0, 0

def append_string(n, x, y):
    if x >= pow(2, n - 1) and y >= pow(2, n - 1):
        return "4", x - pow(2, n - 1), y - pow(2, n - 1)
    elif x >= pow(2, n - 1):
        return "1", x - pow(2, n - 1), y
    elif y >= pow(2, n - 1):
        return "3", x, y - pow(2, n - 1)
    else:
        return "2", x, y

def translate_into_coord(d, x, y):
    if len(d) == 1:
        dx, dy = quadrant(0, d)
        return x + dx, y + dy
    
    else:
        dx, dy = quadrant(len(d) - 1, d[0])
        return translate_into_coord(d[1:], x + dx, y + dy)

def translate_into_str(d, x, y, target_len):
    if len(d) == target_len:
        return d
    else:
        a, nx, ny = append_string(target_len - len(d), x, y)
        return translate_into_str(d + a, nx, ny, target_len)

cy, cx = translate_into_coord(D, 0, 0)
ny = cy - dy
nx = cx + dx
if 0 <= ny < pow(2, int(ln)) and 0 <= nx < pow(2, int(ln)):
    print(translate_into_str("", nx, ny, int(ln)))
else:
    print(-1)