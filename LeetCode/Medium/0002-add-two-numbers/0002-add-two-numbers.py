# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(no1, no2, carry):
            if not no1 and not no2:
                if carry:
                    return ListNode(1)
                else:
                    return
            val1 = no1.val if no1 else 0
            val2 = no2.val if no2 else 0
            cur = ListNode((val1+val2+carry) % 10)
            no1nxt = no1.next if no1 else None
            no2nxt = no2.next if no2 else None
            cur.next = helper(no1nxt, no2nxt, (val1+val2+carry) // 10 )
            return cur
        return helper(l1, l2, 0)