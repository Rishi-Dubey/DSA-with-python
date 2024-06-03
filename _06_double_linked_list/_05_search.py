"""Here I will create search method"""


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self) -> None:
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

    def insert(self, value, location=-1):
        new_node = Node(value)
        if self.head is None:                   # means Double linked list is empty
            self.head = new_node
            self.tail = new_node

        else:
            if location == 0:                   # means add at first node position
                new_node.next = self.head       # new_node now points to old first node
                self.head.previous = new_node   # old first node's previous points to new_node
                self.head = new_node            # head now points to newly created new_node

            elif location == -1:                # want to add in last
                new_node.previous = self.tail   # now new_node previous points to old last node
                self.tail.next = new_node       # old last node now become 2nd last node(so points to new_node)
                self.tail = new_node            # now tail points to new last node
                                                
            else:
                index = 0
                temp_node = self.head
                while index < location -1 and temp_node:  # means till it encounters None(end of DLL)
                    temp_node = temp_node.next
                    index += 1
                
                if index != location -1:   # means location is out of range
                    print("Out of range")
                    return
                
                # now we have the location of node just before the target
                next_node = temp_node.next
                
                # now we will insert the new node in b/w temp_node and next_node
                temp_node.next = new_node       # temp_node's next is now new_node
                new_node.previous = temp_node   # new_nod's previous is now temp_node
                
                new_node.next = next_node       # new_nod's next is now next_node
                next_node.previous = new_node   # next_node previous is now new_node
                
    def show(self):
        nodes_value = []
        node = self.head
        while node:
            nodes_value.append(node.value)
            node = node.next
        print(nodes_value)

    def search(self, value):
        if self.head is None:
            print("Empty Circular Simple Linked List")
            return None
        else:
            node = self.head
            index = 0
            while node:
                if node.value == value:
                    return index
                index += 1
                node = node.next
            print("Value not found")
            return

myDLL = DoubleLinkedList()

[myDLL.insert(i+1) for i in range(5)]

myDLL.show()

index = myDLL.search(4)
print(index)
