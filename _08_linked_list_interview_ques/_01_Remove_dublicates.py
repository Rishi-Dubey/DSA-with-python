# Goal -> To create a program that will remove the duplicate nodes from the linked list

# Here I import the Linked List class that I created
from LinkedList import LinkedList as LL


class Solution(LL):
    def __init__(self) -> None:
        super().__init__()

    def pop(self, location = -1) -> int | None:
        """ Return the removed value of given location or None if not found or list is empty
            It will remove the value at given location(index)
        """

        if self.head is None:
            print("Linked List is empty")
            return None

        else:   # when node/nodes exits
            # only one node exits
            if self.head == self.tail and location in (0, 1):
                value = self.head.value                            # value we will delete
                self.head = None
                self.tail = None
                return value                                       # returning the value we delete

            elif location == 0:                                    # want to remove the first node
                value = self.head.value                            # value we will delete
                # now head points to 2nd node
                self.head = self.head.next
                return value
            
            elif location == -1:                                   # want to remove the last node
                temp_node = self.head                              # will store the last 2nd node
                while temp_node.next != self.tail:
                    temp_node = temp_node.next

                # now we have the 2nd last node(temp_node)
                # become last so points to None
                value = temp_node.next.value
                temp_node.next = None
                self.tail = temp_node                              # points to new last node
                return value                                       # returning the value we delete

            else:                                                  # want to delete other than 1st or last node
                index = 0
                temp_node = self.head                              # node before the target

                while index < location - 1 and temp_node.next != None:
                    temp_node = temp_node.next
                    index += 1

                if index != location - 1:                            # check if it has valid index
                    print("Index Out of range")
                    return None

                # now we have node(temp_node) just before the target
                target_node = temp_node.next
                # temp_node next become target node's next
                temp_node.next = target_node.next

    def found_duplicate(self) -> set[int]:
        duplicates_set : set = set()
        current_node = self.head
        temp_node = self.head.next  # second node
        index = 1
        main_loop_run = 1   # will keep track of how many times first loop runs
        while current_node.next:
            while temp_node:
                if current_node.value == temp_node.value:   # found duplicate
                    if index == len(self) - 1:    # if its last element
                        duplicates_set.add(-1)

                    else:
                        duplicates_set.add(index)           # remove that index value
                index += 1
                temp_node = temp_node.next
            current_node = current_node.next       # become's its next node
            temp_node = current_node.next          # it becomes current nodes next
            main_loop_run += 1
            index = main_loop_run                   # index of temp_node(since it become's current.next.next) means 2
        
        return duplicates_set
    
    def remove_duplicate(self):
        duplicate_list = sorted(self.found_duplicate(), reverse=True)
        
        if len(duplicate_list) == 0:
            print("No duplicate found")
        else:
            for index in duplicate_list:
                self.pop(index)
        print("Duplicate nodes removed Successfully")
        
LL = Solution()

LL.add(1)
LL.add(1)
LL.add(1)
LL.add(5)
LL.add(8)
LL.add(9)

[LL.add(i) for i in range(11)]
print(LL)
print(len(LL))


LL.remove_duplicate()

print(LL)
print(len(LL))
