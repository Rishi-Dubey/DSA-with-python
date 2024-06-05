""" Program that will find the nth element value from the last node
    We can't use the len method"""
    
from LinkedList import LinkedList

class Solution(LinkedList):
    def __init__(self) -> None:
        super().__init__()
    
    def find(self, n : int) -> int | None:
        """ Return the value of given nth index from the last node or None if not found
            Takes n-> Index from the last node
            if n = 1 -> return value of last node and so on.."""
        
        if self.head is None:
            print("Linked List is empty")
            return None
        
        else:
            # now we will create two pointer each (n) nodes apart
            # when the 2nd pointer will reach the last node. 1st pointer will be at out target location
            
            pointer1 = self.head
            pointer2 = self.head
            # if n = 1(means user wants the last node value) so both pointer should be as same location
            index = 0
            while index < n - 1 and pointer2 is not None:   # if pointer2 is None means it goes out of range
                pointer2 = pointer2.next
                index += 1
            
            # checking if it has valid range
            if pointer2 is None:
                print("Index Out of range")
                return None

            # moving both pointers until pointer2 become last node
            while pointer2 != self.tail:
                pointer2 = pointer2.next
                pointer1 = pointer1.next
            
            # now we have out target index location from the last(pointer1)
            return pointer1.value

sol = Solution()

[sol.add(i) for i in range(10)]
print(sol)

result = sol.find(4)
print(result)