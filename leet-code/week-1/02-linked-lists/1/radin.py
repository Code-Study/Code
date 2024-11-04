class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # 첫번째 포인터를 n+1 만큼 앞으로 보내기
        for _ in range(n + 1):
            first = first.next
            
        # 두 포인터를 이동하기 - 첫번째 포인터가 마지막에 도달할때까지
        while first:
            first = first.next
            second = second.next
        
        # 두번쨰포인터.next는 없앨 노드임
        second.next = second.next.next
        
        return dummy.next
