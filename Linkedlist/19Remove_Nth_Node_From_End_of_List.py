##medium
## 36ms, 94.25%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        headcp=head
        if not headcp.next:
            return None
        cnt=1
        while headcp.next:
            headcp=headcp.next
            cnt+=1
        pos=cnt-n-1
        if cnt==n:
            return head.next
        headcp=head
        while pos>0:
            headcp=headcp.next
            pos-=1
            
        headcp.next=headcp.next.next
        
        return head
            
            
            