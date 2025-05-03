from collections import deque
def solution(stones, k):
    q = deque() # keep it descending

    for i in range(k):
        while q and stones[q[-1]] < stones[i]:
            q.pop()
        q.append(i)
    
    ans = stones[q[0]]
    for i in range(k, len(stones)):
        # is while operation required? what if we use a single condition operation like 'if'
        while q and q[0] <= i - k:
            q.popleft()
        
        while q and stones[q[-1]] < stones[i]:
            q.pop()
        
        q.append(i)
        ans = min(ans, stones[q[0]])

    return ans