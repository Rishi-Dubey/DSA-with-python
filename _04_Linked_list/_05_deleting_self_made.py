# Here I will create Single Linked List add elements to it and traverse through it

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_node(self, value, location):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if location == 0:  # want to add at index 0
                new_node.next = self.head
                self.head = new_node

            elif location == 1:   # want to add in last
                self.tail.next = new_node  # previous last node become points to latest last node
                self.tail = new_node  # tail now points to latest last node
                # new_node.next = None  # new node is last of point to None

            else:  # to add in middle
                # get the first node value(to loop through all the node)
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1

                # We have [1,2,3,4,6,7] we want to insert 5 b/w 4 and 6
                # now we know the location of 4

                next_node = temp_node.next  # location of 6
                temp_node.next = new_node
                new_node.next = next_node

    def show(self):
        my_node = self.head
        array: list = []
        while my_node is not None:
            array.append(my_node.value)
            # print(my_node.value)
            my_node = my_node.next

        print(array)

    def delete(self, value):
        node = self.head
        if self.head is None:
            print("Single Linked List is empty")
        
        else:
            # when value = first_node.value
            if self.head.value == value:
                if self.head.next is None:  # only one node in SLL
                    self.head = None
                    self.tail = None
                    print("Deleted Successfully")
                    
                
                else:                       # more than one node in SLL
                    self.head = self.head.next
                    print("Deleted Successfully")
            
            # when value = last_node.value
            elif self.tail.value == value:
                if self.tail == self.head:  # only one node is SLL
                    self.head = None
                    self.tail = None
                    print("Deleted Successfully")
                    
                else:                       # More than one node
                    node_before_last = self.head
                    while node_before_last:
                        if node_before_last.next == self.tail:
                            break
                        node_before_last = node_before_last.next
                            

                    # now breaking the link with targeted node
                    node_before_last.next = None
                    self.tail = node_before_last
        
Single_Linked_list = SLinkedList()


def add():
    # (value, location) # location = 1(means at last of SLL)
    Single_Linked_list.add_node(1, 1)
    Single_Linked_list.add_node(2, 1)
    Single_Linked_list.add_node(3, 1)
    Single_Linked_list.add_node(4, 1)
    # (value = 0, location = 0) # means at first place
    Single_Linked_list.add_node(0, 0)
    Single_Linked_list.add_node(100, 3)  # adding at location(index) = 3

    Single_Linked_list.show()


add()

Single_Linked_list.delete(0)
Single_Linked_list.show()
Single_Linked_list.delete(4)
Single_Linked_list.show()