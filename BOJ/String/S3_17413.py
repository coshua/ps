s = input()

ans = ""

id = 0
while(id < len(s)):
    if (s[id] == ' '):
        ans += s[id]
        id += 1
    elif (s[id] == '<'):
        tag = "<"
        id += 1
        while (s[id] != '>'):
            tag += s[id]
            id += 1
        ans += tag + '>'
        id += 1
    else:
        word = s[id]
        id += 1
        while (id < len(s) and s[id] != ' ' and s[id] != '<'):
            word += s[id]
            id += 1
        ans += word[::-1]

print(ans)
