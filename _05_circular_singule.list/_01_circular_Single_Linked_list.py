"""Here I will Create Circular Single Linked list
1) Head -> connect to node of first and tail also connect to first node"""

class CSLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
        
    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        return "CSLL is created Successfully"
    
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
          

CircularSLL = CSLinkedList()

CircularSLL.create(1)
print([node.value for node in CircularSLL])

