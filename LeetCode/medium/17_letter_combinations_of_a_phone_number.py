comb = list
def letterCombinations(digits):
    dfs("", digits)
    return comb

def dfs(s, c, comb):
    if len(c) == 0:
        return
    if len(c) == 1:
        for i in possible_digits(c[0]):
            comb.append(s + i)
        return
    for i in possible_digits(c[0]):
        dfs(s + i, c[1])

def possible_digits(c):
    if c == '2':
        return 'abc'
    elif c == '3':
        return 'def'
    elif c == '4':
        return 'ghi'
    elif c == '5':
        return 'jki'
    elif c == '6':
        return 'mno'
    elif c == '7':
        return 'pqrs'
    elif c == '8':
        return 'tuv'
    elif c == '9':
        return 'wxyz'

print(letterCombinations("2"))