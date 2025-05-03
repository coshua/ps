class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        cur_people = 1
        increment = [0] * n
        num_heard_at = [0] * n

        if delay < n:
            increment[delay] = 1
        num_heard_at[0] = 1

        for i in range(1, n):
            if i - forget >= 0:
                increment[i] -= num_heard_at[i - forget]
            
            increment[i] += increment[i - 1]
            num_heard_at[i] = increment[i]
            
            if i + delay < n:
                increment[i + delay] += num_heard_at[i]

            cur_people += increment[i]
            if i - forget >= 0:
                cur_people -= num_heard_at[i - forget]
            cur_people %= 10**9 + 7

        return cur_people