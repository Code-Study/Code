class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = ListNode(next=head)
        start, end = head, head.next

        for _ in range(n-1):
            end = end.next
        
        while end is not None and end.next is not None:
            start = start.next
            end = end.next
            
        start.next = start.next.next
        return head.next