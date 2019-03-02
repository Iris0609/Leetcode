##medium
##linkedlist
##48ms,23.82%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead1=odd=ListNode(0)
        dummyhead2=even=ListNode(0)
        dummyhead1
        
        while head:
            odd.next=head
            even.next=head.next

            odd=odd.next
            even=even.next
            if head.next:
                head=head.next.next
            else:
                head=None
        odd.next=dummyhead2.next
        return dummyhead1.next