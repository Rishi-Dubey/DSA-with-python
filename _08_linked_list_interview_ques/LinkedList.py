"""Here I will create Linked list class
so that I can Import it every time in other programs"""
import random as r


class Node:
    """ Return None
        It will create node
        with node.value = None(default), node.next = None(default) and node.previous = None(default)
    """

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.previous = None

    # when use print the instance of Node class it will run the __str__ function
    def __str__(self) -> str:
        print(str(self.value))


class LinkedList:
    """ Return None 
        Creates empty Linked List
        with head = None and tail = None
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # calls when use loop on instance of LinkedList class
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    # call when print(instance of class)
    def __str__(self) -> str:
        # here self is class means we are call the iter method
        Llist = [str(i.value) for i in self]
        return " -> ".join(Llist)

    # when we use len(instance of class) we call this fx
    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def add(self, value):
        new_node = Node(value)
        if self.head is None:               # when no node exits
            self.head = new_node
            self.tail = new_node

        else:                               # if node/nodes exits add in last
            self.tail.next = new_node       # last element now becomes(2nd last)
            self.tail = new_node            # now tail points to new last node

        return self.tail                    # returns the newly added node

    # method to generate random numbers
    def generate(self, n=1, min_value=0, max_value=10):
        """ Return instance of class
            created linked list with random numbers
            three parameters n, min_value, max_value
            n -> no of nodes you want(default = 1)
            min_value -> minimum value of range you want(default = 0)
            max_value -> maximum value of range you want(default = 10)
            """

        # if use make the already created linked list empty
        self.head = None
        self.tail = None

        # now time to add values
        for i in range(n):
            self.add(r.randint(min_value, max_value))

        return self         # return the instance of class itself


if __name__ == "__main__":
    customLL = LinkedList()
    customLL.generate(10, 0, 100)
    print(customLL)
    print(len(customLL))