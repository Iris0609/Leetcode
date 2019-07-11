#medium
#40ms, 71.45%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return
        dummyhead=ListNode(x-1)
        pre=dummyhead
        pre.next=head
        flag=head
        while flag:
            if flag.val <x:
                pre=flag
                flag=flag.next
            else:
                break
        pre2=flag
        if flag and flag.next:
            cur=flag.next
        else:
            return dummyhead.next
        
        while cur:
            if cur.val>=x:
                pre2=cur
                cur=cur.next
                
            else:
                pre.next=cur
                pre2.next=cur.next
                cur.next=flag
                pre=cur
                cur=pre2.next
                
        return dummyhead.next
                
                
        
        