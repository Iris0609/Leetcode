
##medium
##36ms
##26.8%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        Dummyhead=ListNode(0)
        tmp=Dummyhead
        
        while l1 and l2:
            if l1.val>=l2.val:
                tmp.next=l2
                l2=l2.next
            else: 
                tmp.next=l1
                l1=l1.next
            tmp=tmp.next
            
        if l1==None or l2==None:
            if l1==None and l2!=None:
                tmp.next=l2
                
            elif l1!=None and l2==None:
                tmp.next=l1
            
        return Dummyhead.next