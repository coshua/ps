from collections import deque
str = ""
lst = input().split()
if (lst[0] != '0'):
    str += lst[1]
str += ","
lst = input().split()
if (lst[0] != '0'):
    str += lst[1]
str += ","
lst = input().split()
if (lst[0] != '0'):
    str += lst[1]

s = set([str])

q = deque()
q.append(str)
cur = 1
nxt = 0
cnt = 0
while(q):
    temp = q.popleft()
    a, b, c = temp.split(",")
    if (a.count("A") == len(a) and b.count("B") == len(b) and c.count("C") == len(c)):
        print(cnt)
        break

    if (len(a) > 0):
        target = a[-1]
        newa = a[:len(a) - 1]
        newb = b + target
        newtemp = ",".join([newa, newb, c])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)
        
        newc = c + target
        newtemp = ",".join([newa, b, newc])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)
            
    if (len(b) > 0):
        target = b[-1]
        newb = b[:len(b) - 1]
        newa = a + target
        newtemp = ",".join([newa, newb, c])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)
        
        newc = c + target
        newtemp = ",".join([a, newb, newc])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)

    if (len(c) > 0):
        target = c[-1]
        newc = c[:len(c) - 1]
        newa = a + target
        newtemp = ",".join([newa, b, newc])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)
        
        newb = b + target
        newtemp = ",".join([a, newb, newc])
        if (not newtemp in s):
            s.add(newtemp)
            nxt += 1
            q.append(newtemp)
    
    cur -= 1
    if (cur == 0):
        cur = nxt
        nxt = 0
        cnt += 1
