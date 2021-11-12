s = input()

pipes = 0 # existing pipes on current index
cnt = 0
i = 0
while (i < len(s) - 1):
    if (s[i] == '(' and s[i + 1] == ')'): # mean it is a razor
        cnt += pipes # razor cuts pipes on current index
        i += 1
    else:
        if (s[i] == '('):
            cnt += 1 # when a pipe appears, we count it
            pipes += 1
        else:
            pipes -= 1
    i += 1
    
print(cnt)