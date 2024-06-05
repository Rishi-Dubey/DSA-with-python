""" Program that will create an linked list with partition
    partition will happen around x all the value that are smaller than x will 
    go the left of Linked List and value higher than x will go to right of Linked list."""

from LinkedList import LinkedList


class Solution(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def partition(self, x: int):
        """ Return new Linked List with partition
            x : Value around which partition will happen
            Every value which is less than x will move to left
            and every value which is higher or equal than x will move to right leaving x at center
        """
        if self.head is None:
            print("Empty Linked List")
            return None

        
        # Lets create a current_node which will traverse through the Linked list
        current_node = self.head       # assigning it the first node
        self.tail = self.head       # tail now points to first node also
        
        while current_node is not None:
            next_node = current_node.next   # saving the current_node next value
            # now we will convert our linked list  -> one node linked list(gradually it will become of same size)
            # but with partition that we want
            current_node.next = None    # setting it None making linkedList -> one node linked list(when loop first time run)
            
            if current_node.value < x:      # smaller value goes left of the x means(start of linked list)
                current_node.next = self.head
                self.head = current_node    # head now points to value smaller than x
            
            else:   # bigger value than x add to right (means at last index place)
                self.tail.next = current_node   # previous last node now points to new last node
                self.tail = current_node    # now last element points to value bigger than x
                
            current_node = next_node
        
        # if by chance tail.next is not None we will set it
        if self.tail.next is not None:
            self.tail = None

        print("Partition done successfully")
        return self


ll = Solution()
[ll.add(i) for i in range(10, 0, -1)]

print(ll)

print(ll.partition(5))
