class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode()
        head = dummy
        smallest = None
        while (True):
            smallest = None
            for node in lists:
                if node != None:
                    if smallest == None:
                        smallest = node
                    elif node.val < smallest.val:
                        smallest = node
            if smallest == None:
                break
            head.next = smallest
            head = smallest
            smallest = smallest.next
        
        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    dummy = ListNode(0)
    dummy.next = head = ListNode(1)
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    print(solution.mergeKLists([dummy.next]))