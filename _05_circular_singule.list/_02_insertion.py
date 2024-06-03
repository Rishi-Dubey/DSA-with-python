# Here I will create method for insertion in Circular Linked list
# Insertion will have two parameters(value, location)
# location(0 for first place),(1 for last),(any other index)


# Just create a node
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    

class CircularSLS:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    
    def show(self):
        node_values = []
        
        node = self.head
        while node:
            node_values.append(node.value)
            if node.next == self.head:
                break
            node =  node.next
        
        print(node_values)
    
    def insert(self, value, location):
        # first we need to create an node
        node = Node(value)
        
        if location == 0:  # add at first position
            if self.head is None: # means an empty Circular Single LL
                self.head = node
                self.tail = node
                node.next = node # points to itself
            
            else:  # one or more node already exits
                node.next = self.head  # new first node points to old first node
                self.head = node   
                self.tail.next = node  # last node points to new first node
                
        # means want to add in last    
        elif location == 1:
            if self.tail is None:  # means an empty Circular Single LL
                self.head = node
                self.tail = node
                node.next = node
            
            else:
                node.next = self.head  # now new last node points to first node
                self.tail.next = node  # previous last node now points to new last node
                self.tail = node       # tail points to new last node
        
        else:
            # now we want to add to an specific location
            # we have CSLL = [0,1,2,3,5,6] we want to add 4 at location 4
            # so we need the reference of node.value(3)
            
            temp_node = self.head
            index = 0
            # condition 2 will ensure that we don't run loop more than one
            while index < location - 1 and temp_node.next != self.head:
                temp_node = temp_node.next
                index += 1
            
            # we get the location greater than one
            if index != location -1 :  # In that case while will stops at last index
                print("Index Out of bound")
                return
            
            # getting the index of example's nodevalue(5)
            next_node = temp_node.next
            node.next = next_node  # new node now points to next node
            temp_node.next = node  # node just before the location now points to newly created node
            


csll = CircularSLS()

csll.insert(0,1)
csll.insert(1,1)
csll.insert(2,1)
csll.insert(3,1)
csll.insert(5,1)
csll.insert(7,1)
csll.insert(8,1)

csll.show()

csll.insert(4,4) 
csll.insert(6,6)
# csll.insert(100, 100)
csll.show() 