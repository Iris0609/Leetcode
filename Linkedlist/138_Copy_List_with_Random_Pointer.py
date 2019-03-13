
##medium
##48ms beats 100%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p=head
        ## insert a copynode after the origin node
        while p:
            newNode=Node(0,None,None)
            newNode.val=p.val
            newNode.next=p.next
            p.next=newNode
            p=newNode.next
        
        ## random copy
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
        
        ## eliminate tmp node
        p=head
        newhead=head.next
        np=newhead
        
        while np.next:
            p.next=np.next
            p=np.next
            np.next=p.next
            np=np.next
            
        p.next=None
        np.next=None

        return newhead


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node



                
                
        