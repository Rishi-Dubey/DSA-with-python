"""Here I will create double Linked list as name suggested.
It's every node have two have connection node.next, node.previous"""

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.previous = None
    

class DoubleLinkedList:
    def __init__(self) ->  None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        print("Double Linked List created Successfully")
    
        
        
myDLL = DoubleLinkedList()
myDLL.create(4)

print([node.value for node in myDLL])