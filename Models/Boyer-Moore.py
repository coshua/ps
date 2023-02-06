# majority voting algorithm

def voting(lst):
    candidate, cnt = 0, 0
    for value in lst:
        if cnt == 0:
            candidate, cnt = value, 1
        if candidate == value:
            cnt += 1
        else:
            cnt -= 1
    
    return candidate if lst.count(candidate) > len(lst) // 2 else -1
