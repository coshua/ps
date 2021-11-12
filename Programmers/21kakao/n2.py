from collections import defaultdict
from collections import deque
def comb(str):
    q = deque()
    q.append(("", 0))
    answer = list()

    while (q):
        temp, id = q.popleft()
        if (id == len(str)):
            if (len(temp) > 1):
                answer.append(temp)
        else:
            q.append((temp, id + 1))
            q.append((temp + str[id], id + 1))
    
    return answer

def solution(orders, course):
    d = defaultdict(int)
    for order in orders:
        order = sorted(order)
        lst = comb(order)
        for food in lst:
            d[food] += 1
    
    answer = list()
    cand = []
    mcnt = 0
    for i in course:
        mcnt = 0
        cand = []
        for x in d:
            if(len(x) == i and d[x] > 1):
                if (d[x] > mcnt):
                    mcnt = d[x]
                    cand = [x]
                elif (d[x] == mcnt):
                    cand.append(x)
        
        for sel in cand:
            answer.append(sel)
    
    answer.sort()
    return answer

tempo = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
tempc = [2, 3, 5]
solution(tempo, tempc)