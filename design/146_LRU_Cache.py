##design
##hard

##1. use orderdict
##108ms,89.06%

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity=capacity
        
        
    def get(self, key: int) -> int:
        if not key in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]
        
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


##2. use hashmap & doublelinkedlist
##152 ms, 39.47%

class DLinkedNode():
    def __init__(self):
        self.key=0
        self.value=0
        self.pre=None
        self.next=None


class LRUCache():
    def _add_node(self,node):
        node.pre=self.head
        node.next=self.head.next
     
        self.head.next.pre=node
        self.head.next=node
    
    def _remove_node(self,node):        
        node.pre.next=node.next
        node.next.pre=node.pre

    
    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        res=self.tail.pre
        self._remove_node(res)
        return res
        
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dl={}
        self.size=0
        self.head,self.tail=DLinkedNode(),DLinkedNode()
        
        self.head.next=self.tail
        self.tail.pre=self.head
              
    def get(self, key: int) -> int:
        node=self.dl.get(key,None)
        if not node:
            return -1
        else:
            self._move_to_head(node)
            return node.value
        
        
    def put(self, key: int, value: int) -> None:
        node=self.dl.get(key)
        if node:   
            node.value=value
            self._move_to_head(node)
        else:
            node=DLinkedNode()
            node.key=key
            node.value=value
            self.dl[key]=node
            self._add_node(node)
            self.size+=1
            
            if self.size>self.capacity:
                tail=self._pop_tail()
                del self.dl[tail.key]
                self.size-=1


            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


            
