"""Here I will create "Circular Doubly Linked List" 
and Implement reverse traversal method named (reverse_show)"""


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
    
    def create(self, value):            # means to use when no nodes exits  with an single value
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.previous = self.tail                # points to last node(In this case itself)
        print("Circular Double Linked List created Successfully")

    def insert(self, value, location = -1):         # default location is last node place
        newNode = Node(value)
        if self.head is None:                       # when No node exists
            self.create(value)                      # calls the already created method
        
        else:   # when node/nodes exits already
            if location == 0:                       # add at index(0)
                newNode.next = self.head            # points to old first node(becomes 2nd)
                newNode.previous = self.tail        # point to last node(making an circle)
                self.head.previous = newNode        # old first node(now last) previous points to newNode
                self.tail.next = newNode            # last node points to first node
                self.head = newNode                 # head now points to new first node
            
            elif location == -1:                    # wants to add to last index
                newNode.next = self.head            # new last node(i.e 2nd) points to first node
                newNode.previous = self.tail        # new last node points to first node
                self.head.previous = newNode        # first node previous is new last node
                self.tail.next = newNode            # old last node now points to new last node
                self.tail = newNode                 # tail now points to new last node
                    
            else:
                index = 0
                temp_node = self.head
                
                # 2nd condition make sure it don't repeats in circular double node(loop)
                while index < location -1 and temp_node.next != self.head:
                    temp_node = temp_node.next
                    index += 1
                
                # Ensure that we have valid range
                if index != location -1:
                    print("Index out of range")
                    return
                
                # now we got the node(temp_node) just before the intended location
                next_node = temp_node.next          # node at next position of our intended location
                
                # time to insert
                temp_node.next = newNode            
                newNode.previous = temp_node
                newNode.next = next_node
                next_node.previous = newNode
            
    def reverse_show(self):
        node = self.tail
        list_node = []
        while node:
            list_node.append(node.value)
            node = node.previous
            if node == self.tail:
                break
        print(list_node)
              
CDLL = CircularDoublyLinkedList()

# CDLL.create(100)
CDLL.reverse_show()
[CDLL.insert(i) for i in range(11)]
CDLL.reverse_show()