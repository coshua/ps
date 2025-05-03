class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        waiting_sum = 0
        timer = 0
        for cx in customers:
            if timer <= cx[0]:
                waiting_sum += cx[1]
                timer = sum(cx)
            else:
                waiting_sum = timer - cx[0] + cx[1]
                timer += cx[1]
        
        return waiting_sum / len(customers)