"""Here I will implement stack method using linked list for o(1) time complexity
It will also have a min method which will return min value but it should be o(1) time complexity"""

class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.top : Node = None
        self.min_node =  None   # an node points to min value -> 2nd min value -> 3rd min value ....
    
    def min(self):
        if self.min_node is None:
            return None
        return self.min_node.value

    def push(self, value):
        # we store the min value every time user inserts an new element even if min is same
        if self.min_node and self.min_node.value < value  :
            # since value > min_node.value we did't change min value just point to newNode(with same value)
            self.min_node = Node(value = self.min_node.value, next = self.min_node)
        
        # when user enters new min or first time insert value
        else:
            self.min_node = Node(value, next=self.min_node)   
            
        # now adding it to stack
        self.top = Node(value, next=self.top)
        
    def pop(self):
        if self.top is None:
            return None
        # since we store min_node of each node of stack(it will point to minNode when one element was short)
        self.min_node = self.min_node.next
        value = self.top.value
        self.top = self.top.next
        return value

custom_stack = Stack()

print(custom_stack.min())
custom_stack.push(1)
custom_stack.push(-1)
custom_stack.push(-2)
print(custom_stack.min())
custom_stack.push(4)
print(custom_stack.min())
custom_stack.pop()
print(custom_stack.min())
custom_stack.push(-11)
print(custom_stack.min())