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
            node = node.next

        print(node_values)

    def insert(self, value, location):
        # first we need to create an node
        node = Node(value)

        if location == 0:  # add at first position
            if self.head is None:  # means an empty Circular Single LL
                self.head = node
                self.tail = node
                node.next = node  # points to itself

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
            if index != location - 1:  # In that case while will stops at last index
                print("Index Out of bound")
                return

            # getting the index of example's nodevalue(5)
            next_node = temp_node.next
            node.next = next_node  # new node now points to next node
            temp_node.next = node  # node just before the location now points to newly created node

    def delete(self, location):
        if self.head is None:
            print("Circular Linked List is empty")
            return None
        
        else: # when CLL is not empty
            if location == 0:  # want to delete first node
                value = self.head.value  # value we want to return and delete
                if self.head.next == self.head:   # means CLL have only one node
                    self.head = None
                    self.tail = None

                else:   # when CLL have more than one node
                    self.head = self.head.next  # head now points to first nodes next(2nd node)
                    self.tail.next = self.head  # last node now points to new first node(2nd become 1st node)
                    
                return value  # returns the deleted value

            if location == 1:  # wants to delete last node
                value = self.tail.value
                if self.head.next == self.head:   # means CLL have only one node
                    self.head = None
                    self.tail = None
                
                else:
                    temp_node = self.head
                    while True:
                        if temp_node.next == self.tail:  # if its next is last element break i.e found last 2nd
                            break
                        temp_node = temp_node.next
                
                    # now we have last second element
                    temp_node.next = self.head      # new last node now points to first node
                    self.tail = temp_node           # tail now have reference of new last node
                return value  # returns the deleted value

            else:  # delete at other location than first and last(0 and 1)
                index = 0
                temp_node = self.head
                
                while index < location -1 and temp_node.next != self.head:
                    temp_node = temp_node.next
                    index += 1
                
                if index != location -1 :  # means user enter location value very high
                    print("Index out of range")
                    return
                
                # now we have location just before the target( which is temp_node)
                targeted_node = temp_node.next  # our target which to delete
                value = targeted_node.value    # value we want to delete and return
                
                temp_node.next = targeted_node.next  # target's next  become temp_node next
                return value   # return the value we just deleted
                
                
csll = CircularSLS()


def all_work():
    csll.insert(0, 1)
    csll.insert(1, 1)
    csll.insert(2, 1)
    csll.insert(3, 1)
    csll.insert(5, 1)
    csll.insert(7, 1)
    csll.insert(8, 1)

    csll.show()

    csll.insert(4, 4)
    csll.insert(6, 6)
    # csll.insert(100, 100)


# all_work()
csll.show()

csll.insert(0,0)
csll.insert(1,1)
csll.insert(2,1)
csll.delete(0)
csll.delete(1)


# csll.delete(1)
# csll.delete(2)
csll.show()
