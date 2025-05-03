class Solution:
    def isPalindrome(self, head) -> bool:
        slow = fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        tempPrev = None

        while slow != None:
            tempNext = slow.next
            slow.next = tempPrev
            tempPrev = slow
            slow = tempNext
        
        while slow != None:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next
        
        return True