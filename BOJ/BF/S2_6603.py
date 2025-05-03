import sys
input = sys.stdin.readline

def backtracking(lst):
    sz = len(lst)
    def dfs(idx, sub_lst):
        if len(sub_lst) == 6:
            print(*sub_lst)
        elif idx >= sz:
            return
        else:
            for j in range(idx, sz - 6 + len(sub_lst) + 1):
                nxt_lst = sub_lst[:]
                nxt_lst.append(lst[j])
                dfs(j + 1, nxt_lst)
    for i in range(0, sz - 6 + 1):
        dfs(i + 1, [lst[i]])

inp = input()
while len(inp) > 2:
    backtracking(list(map(int, inp.split()))[1:])
    print()
    inp = input()