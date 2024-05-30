# Insertion methods in linked list

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):  # work when we call using a loop(using a loop in Reference of SLinkedList)
        node = self.head
        while node:
            yield node
            node  = node.next
    
    #insert in Lined list
    def add_node(self, value, location):    
        new_Node = Node(value)  # creating an instance of new node with class(Node)
        if self.head is None:   # if there not a single not present
            self.head = new_Node  # storing the reference(means use (self.head or new_Node) is same)
            self.tail = new_Node
        
        else :  
            if location == 0:  # wants to add in first place(i.e at index 0)
                new_Node.next = self.head  # head have stored the value of previous first node
                self.head = new_Node
            
            elif location == 1:  # want to add in last place(i.e at index (len -1) )
                new_Node.next = None  # since it become last node
                self.tail.next = new_Node  # means pervious last become 2nd last(store the reference of new_update last value(self.tail.next means the pervious last next))
                
                self.tail = new_Node  # now tail will have reference of new Last node
            
            else : 
                temp_node = self.head  # get the first node reference(till find location)
                index = 0  # will go to until find the desired location to insert
                
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                
                # now we are at the desired location(with temp_node) means location -1 index
                # we want to insert new_Node between temp_node and next_node
                # suppose we want to insert 5 (we have now 4(temp_node)) and (6 as next_node)
                next_node = temp_node.next # get the (ex's 6 reference)
                temp_node.next = new_Node  # get the new_node's reference 
                
                new_Node.next = next_node  # new Node get reference of it next node
            
            
# Lets create a linked list reference and insert value

Single_Linked_list = SLinkedList()

Single_Linked_list.add_node(1, 1)  #(value, location) # location = 1(means at last of SLL)
Single_Linked_list.add_node(2, 1)
Single_Linked_list.add_node(3, 1)
Single_Linked_list.add_node(4, 1)
Single_Linked_list.add_node(0, 0)  #(value = 0, location = 0) # means at first place
Single_Linked_list.add_node(100, 3)  # adding at location(index) = 3

print([Nodwa.value for Nodwa in Single_Linked_list])