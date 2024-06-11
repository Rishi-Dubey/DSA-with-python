"""Here I will implement Queue and all its methods using two different stacks
Queue(FIFO) -> First In First Out
Stack(LIFO) -> Last In Last Out

Stack(1) will be used to store all the values
Stack(2) will be used when user use Dequeue it will store all the value from stack1 in reverse order making it like queue
then after dequeue it will transfer all the value back again.
"""

class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def __len__(self):
        return len(self.stack)
    
    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            return self.stack.pop()
    def __str__(self) -> str:
        return str(self.stack)

class QueueViaStack:
    def __init__(self) -> None:
        self.StackIn = Stack()
        self.StackOut = Stack()
    
    def enqueue(self, value):
        self.StackIn.push(value)
    
    def dequeue(self):
        if len(self.StackIn) == 0:
            print("Empty Queue")
            return None
        """Queue -> First in First out
        stack -> Last in Last out
        So if first Stack goes empty by pop its index(0) element will become last index
        element of stack2 and pop will remove it making it work like Queue.
        """
        while len(self.StackIn) != 0:
            self.StackOut.push(self.StackIn.pop())
        
        value = self.StackOut.pop()
        while len(self.StackOut) != 0:
            self.StackIn.push(self.StackOut.pop())
        
        return value
    
    def __str__(self) -> str:
        return f"Queue : {self.StackIn.stack}"
    
cs = QueueViaStack()
cs.enqueue(1)
cs.enqueue(2)
cs.enqueue(3)
print(cs)
print(cs.dequeue())
print(cs.dequeue())
print(cs.dequeue())
print(cs.dequeue())