"""Here I will create "Circular Doubly Linked List" 
and Implement delete method"""


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
            
    def show(self):
        node = self.head
        list_node = []
        while node:
            list_node.append(node.value)
            node = node.next
            if node == self.head:
                break
        print(list_node)
      
    def search(self, value) -> int | None:
        if self.head is None:       # Means no node exit
            print("List is empty")
            return None
        
        else:   # when one or more node exits
            index = 0               # will store the index where value matched
            temp_node = self.head
            while True:
                if temp_node.value == value:    # Match found
                    return index
                index += 1
                temp_node = temp_node.next
                if temp_node == self.head:       # Means one loop of list is complete
                    print("Value not found")
                    return None
            
    def delete(self, location = -1) -> int | None:        # Assumes the default location is last node
        if self.head is None:
            print("List is empty")
            return None
        
        else:   # One or more node exits
            if self.head == self.tail and location in (0, -1):  # only one not exits
                value = self.head.value                 # value we want to delete
                self.head = None
                self.tail = None
                return value
                
            # Here we know if first condition is False
            # we have more than one node in list
            elif location == 0:                         # want to delete the first node
                value = self.head.value                 # value we want to delete
                new_first_node = self.head.next         # actually (2nd) now will become first
                new_first_node.previous = self.tail     # since it becomes (1st)
                self.head = new_first_node
                return value

            elif location == -1:
                value = self.tail.value                 # value we want to delete
                new_last_node = self.tail.previous      # actually (2nd last) now will become last
                new_last_node.next = self.head          # point to first node
                self.tail = new_last_node               # tail now points to new last node
                return value
            
            else:                                       # delete at any other given location
                index = 0
                temp_node = self.head                   # used to loop through the list
                while index < location -1 and temp_node.next != self.head:
                    temp_node = temp_node.next
                    index += 1
                
                # check if it has valid range
                if index != location -1:
                    print("Out of range")
                    return None

                # now we have the temp_node which is node just before the target
                target_node = temp_node.next
                
                temp_node.next = target_node.next
                target_node.previous = temp_node
                                                      
    def clearAll(self):
        self.head = None
        self.tail = None
        
CDLL = CircularDoublyLinkedList()

# CDLL.create(100)
CDLL.show()
[CDLL.insert(i+10) for i in range(11)]
CDLL.show()

CDLL.delete(5)
CDLL.delete(0)
CDLL.delete()
CDLL.delete()

CDLL.show()
CDLL.clearAll()
CDLL.show()