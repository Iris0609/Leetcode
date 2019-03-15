
##stack design
##easy
##36ms,58.03%

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        self.size=0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.size+=1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size>0:
            res=self.stack[0]
        else:
            return None
        if self.size>1:
            self.stack=self.stack[1:]
            self.size-=1
        else:
            self.stack=[]
            self.size=0
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size>0:
            return self.stack[0]
        else:
            return None
    

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()