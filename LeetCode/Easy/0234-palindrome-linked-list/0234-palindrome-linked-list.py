# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dum = ListNode()
        dum.next = head
        fast = slow = dum
        cnt = 0
        prev = dum
        while fast and fast.next:
            cnt +=1
            prev = fast.next
            fast = fast.next.next
            slow = slow.next
        
        nxt = slow.next
        slow.next = None
        prev = slow
        slow = nxt
        while slow:
            nxt  =slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        tail = prev
        while tail and head:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True


