# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        
        onestep = head.next
        twostep = None
        head.next = None
        while onestep != None:
            twostep = onestep.next
            onestep.next = head
            head = onestep
            onestep = twostep
        
        return head
            