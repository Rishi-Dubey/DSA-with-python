"""Here I will create "Circular Double Linked List" 
Its all nodes are connect two each other in two way node.next and node.previous
Also its last node points to first node
and first node points to last making An Circular formation of nodes"""


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.previous = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        temp_node = self.head
        while True:
            yield temp_node
            temp_node = temp_node.next
            if temp_node == self.head:
                break
    
    def create(self, value):      # means to use when no nodes exits  with an single value
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.previous = self.tail   # points to last node(In this case itself)
        print("Circular Double Linked List created Successfully")


CDLL = CircularDoublyLinkedList()

CDLL.create(100)
print([node.value for node in CDLL])