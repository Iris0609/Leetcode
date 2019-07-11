# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#medium
#36ms, beats 94.90%
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if k==0:
            return head
        
        cnt=1
        dummyhead=head
        while head.next:
            cnt+=1
            head=head.next
        head=dummyhead  
        if cnt>=k:
            tmp=cnt-k
        elif k%cnt==0:
            tmp=0
        else:
            tmp=cnt-k%cnt
            
        if tmp==0:
            return dummyhead
        while tmp>1:
            head=head.next
            tmp-=1

        newhead=head.next
        head.next=None
        head=newhead
        while head.next:
            head=head.next
        head.next=dummyhead



        return newhead
                
            
            