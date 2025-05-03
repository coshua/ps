# two pointers traverse the linked list
# if pointers meet at some point, a loop exists
# if the fast pointer meets the end, no loop exists

def detectLoop(head):
    slow, fast = head, head

    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    
    return 0