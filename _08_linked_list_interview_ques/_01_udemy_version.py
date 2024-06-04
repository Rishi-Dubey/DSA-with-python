from LinkedList import LinkedList


class RemoveDuplicate(LinkedList):
    def __init__(self) -> None:
        super().__init__()
    
    def duplicate_remove(self) -> None:
        if self.head is None:
            return None
        
        visited_nodes : set = set([self.head.value])    # for efficiency
        current_node = self.head    # used to traverse through linked list
        
        while current_node.next is not None:    # means 2nd node -> last 2nd node
            if current_node.next.value in visited_nodes:      # since we know first value can't be duplicate(means self.head)
                if current_node.next == self.tail:   # means we found last node is duplicate
                    self.tail = current_node
                current_node.next = current_node.next.next  # set it 2nd node to 4 node
            else:
                visited_nodes.add(current_node.next.value)
                current_node = current_node.next
        
ll = RemoveDuplicate()

[ll.add(i) for i in range(5)]
ll.add(0)
ll.add(1)

print(ll)

ll.duplicate_remove()
print(ll)