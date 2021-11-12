


def trans(str):
    ans = []
    lst = str.split()
    if (lst[0] == "java"):
        ans.append(0)
    elif (lst[0] == "cpp"):
        ans.append(1)
    else:
        ans.append(2)
    
    if (lst[1] == "backend"):
        ans.append(0)
    else:
        ans.append(1)

    if (lst[2] == "junior"):
        ans.append(0)
    else:
        ans.append(1)
    
    if (lst[3] == "chicken"):
        ans.append(0)
    else:
        ans.append(1)

    ans.append(int(lst[4]))
    return ans


def solution(info, query):
    m = [[[[[0] * 261 for c in range(2)] for c in range(2)] for b in range(2)] for a in range(3)]
    for i in info:
        a, b, c, d, e = trans(i)
        m[a][b][c][d][e] += 1
    
    for i in range(1, 261):
        for j in range(3):
            for k in range(2):
                for n in range(2):
                    for o in range(2):
                        m[j][k][n][o][261 - i - 1] += m[j][k][n][o][261 - i]
    
    answer = []

    for i in query:
        q = i.split()

        a = []
        if (q[0] == "java"):
            a.append(0)
        elif (q[0] == "cpp"):
            a.append(1)
        elif (q[0] == "python"):
            a.append(2)
        else:
            a.append(0)
            a.append(1)
            a.append(2)
        
        b = []
        if (q[2] == 'backend'):
            b.append(0)
        elif (q[2] == 'frontend'):
            b.append(1)
        else:
            b.append(0)
            b.append(1)
        
        c = []
        if (q[4] == 'junior'):
            c.append(0)
        elif (q[4] == 'senior'):
            c.append(1)
        else:
            c.append(0)
            c.append(1)
        
        d = []
        if (q[6] == 'chicken'):
            d.append(0)
        elif (q[6] == 'pizza'):
            d.append(1)
        else:
            d.append(0)
            d.append(1)
        
        e = int(q[7])

        ans = 0
        for f in a:
            for g in b:
                for h in c:
                    for z in d:
                        ans += m[f][g][h][z][e]
        
        answer.append(ans)

    return answer

tempinfo = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
tempq = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(tempinfo, tempq)