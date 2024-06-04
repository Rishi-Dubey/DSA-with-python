# Goal -> To create a program that will remove the duplicate nodes from the linked list

# Here I import the Linked List class that I created
from LinkedList import LinkedList as LL


class Solution(LL):
    def __init__(self) -> None:
        super().__init__()

                
    def found_duplicate(self) -> list[int]:
        duplicates_set : set = set()                # will store the index of duplicate values
        data : dict = {}                            # will store the value and their index
        current_node = self.head                    # used to iterate through the Linked List
        index = 0                                   # will store the index of all the nodes
        while current_node:
            if current_node.value in data:          # found duplicate 
                duplicates_set.add(index)           # store the index of duplicate
            
            else:
                data[current_node.value] = index    # store the value : index pair
            current_node = current_node.next
            index += 1
        
        return sorted(duplicates_set, reverse=True)
        
    def remove_duplicate(self) -> None:
        duplicate_list = self.found_duplicate()
        
        if len(duplicate_list) == 0:
            print("No duplicate found")
        else:
            for index in duplicate_list:
                self.pop(index)
        print("Duplicate nodes removed Successfully")


def run() -> None:     
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

run()