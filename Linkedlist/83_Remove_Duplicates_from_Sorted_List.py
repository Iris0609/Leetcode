
#easy
#48ms, beats 67.98%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        pre=head
        dummyhead=head
        while head.next:
            head=head.next
            if head.val==pre.val:
                pre.next=head.next
            else:
                pre=head
        return dummyhead
        