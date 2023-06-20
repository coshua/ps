# pick k random elements from collections size n >= k
import random
def reservoir_sampling(lst, k):
    ans = lst[:k]

    for i in range(k, len(lst)):
        j = random.randrange(0, i + 1)
        if j < k:
            ans[k] = j
    
    return ans