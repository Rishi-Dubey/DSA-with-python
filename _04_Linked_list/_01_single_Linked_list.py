"""Here I will Create Single Linked list
1) Head -> connect to node of first and first is connect to Tail"""

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


single_Linked_list = SLinkedList()

node1 = Node(1)
node2 = Node(2)


single_Linked_list.head = node1
single_Linked_list.head.next = node2

single_Linked_list.tail = node2

print(f"Node1 value: {single_Linked_list.head.value}\nNode1 next : {single_Linked_list.head.next}")