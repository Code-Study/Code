# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0, head)
        first = ans
        second = ans
        
        # 첫 노드를 n+1만큼 이동시킴
        for _ in range(n+1):
            first = first.next
        
        # first가 끝까지 이동했을 때 second의 위치는 뒤에서 n번째
        while first:
            first = first.next
            second = second.next
        
        # 해당 위치를 제거
        second.next = second.next.next
    
        return ans.next