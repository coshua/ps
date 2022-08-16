def generateParenthesis(n):
    comb = list()

    def dfs(s, n_open, n_close):
        if n_open == n and n_close == n:
            comb.append(s)
            return
        
        if n_open == n_close:
            dfs(s + "(", n_open + 1, n_close)
        
        else:
            if n_open < n:
                dfs(s + "(", n_open + 1, n_close)
            if n_close < n:
                dfs(s + ")", n_open, n_close + 1)
    
    dfs("", 0, 0)
    return comb