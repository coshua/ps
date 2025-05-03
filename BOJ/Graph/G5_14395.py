from collections import deque
s, t = list(map(int, input().split()))

v = False

match = ""
qnum = deque()
qop = deque()
lst = []
qnum.append(s)
qop.append("")
while (qnum):
    num = qnum.popleft()
    op = qop.popleft()
    if (num == t):
        if (match == ""):
            match = op
        else:
            if (len(match) == len(op)):
                match = min(match, op)
            else:
                if (len(match) > len(op)):
                    match = op

    else:
        if (not v):
            qnum.append(1)
            qop.append(op + "/")
            v = True
    
        if (num * 2 <= t):
            qnum.append(num * 2)
            qop.append(op + "+")

        if (num != 1 and num * num <= t):
            qnum.append(num * num)
            qop.append(op + "*")

if (s == t):
    print(0)
elif (match == ''):
    print(-1)
else:
    print(match)