##hard
##92ms, 61.32%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge2list(l1,l2):
            tmphead=ListNode(0)
            track=tmphead
            while l1 and l2:
                if l1.val<=l2.val:
                    track.next=l1
                    l1=l1.next
                else:
                    track.next=l2
                    l2=l2.next
                track=track.next
            else:
                if l1:
                    track.next=l1
                if l2:
                    track.next=l2

            return tmphead.next
        
        
        
        if not lists:
            return None

        amount=len(lists)
        interval=1
        
        while amount>interval:
            for i in range(0,amount-interval,2*interval):
                lists[i]=merge2list(lists[i],lists[i+interval])
            interval*=2
        return lists[0]
    
        
            
                
                
                

       
        
        
            
        
                
            
            
            
            
     