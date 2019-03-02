##easy
##linkedlist
##204ms,76.32%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1=headA
        node2=headB
        while node1 is not node2:
            node1=headB if not node1 else node1.next
            node2=headA if not node2 else node2.next
        
        return node1