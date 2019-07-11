
#medium
#36ms,beats 73.28%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        rehead=ListNode(None)
        dummyhead=head
        cnt=0
        h=None
        t=None
        
        if m==n:
            return head
        while head:
            cnt+=1
            if m<=cnt<=n:
                if cnt==m:
                    pret=head
                nxt=head.next
                head.next=rehead.next
                rehead.next=head
                head=nxt
                
            elif cnt==m-1:
                h=head
                head=head.next
            elif cnt==n+1:
                t=head
                head=head.next
            else:
                head=head.next
        if h:
            h.next=rehead.next
        else:
            dummyhead=rehead.next
        if pret:
            pret.next=t
            
        return dummyhead
                
        
                
        