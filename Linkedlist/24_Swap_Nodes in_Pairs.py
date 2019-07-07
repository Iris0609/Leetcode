
# 52s, beats 13.56%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        
        dummyhead=head.next
        forehead=None
        while head:
            tmp=head.next
            if not tmp:
                break
            if forehead:
                forehead.next=tmp 
            head.next=tmp.next
            tmp.next=head
            forehead=head
            head=head.next

            
        return dummyhead