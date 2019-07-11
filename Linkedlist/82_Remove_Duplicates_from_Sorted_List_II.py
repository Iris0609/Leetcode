
#medium
#48ms, beat66.27%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummyhead=ListNode('a')                
        pre=dummyhead
        cur=head
        tmp=cur.val-1
        nxt=cur.next
        while cur:
            if not nxt and cur.val!=tmp:
                pre.next=cur
                break
            elif not nxt and cur.val==tmp:
                pre.next=cur.next
                break
            if cur.val!=tmp and cur.val!=nxt.val:
                tmp=cur.val
                pre.next=cur
                pre=cur
                cur=nxt
                nxt=cur.next
            else:
                tmp=cur.val
                cur=nxt
                nxt=cur.next
                         
                
        return dummyhead.next
                
            
                
            
        
        
        
        
        
        
        
        
       
        
      
        
            
                
        
        
        
        