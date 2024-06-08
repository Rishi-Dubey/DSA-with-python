"""Program will find the intersection points of two linked list and return 
the intersection node.
Note -> Intersection is compared by node reference not the value"""

from LinkedList import LinkedList, Node

class Solution(LinkedList):
    def __init__(self) -> None:
        super().__init__()
    
    def intersection(self, LL1: LinkedList, LL2: LinkedList):
        # assume
        temp_node = LL1.head
        bigger_ll = LL1
        if len(LL1) > len(LL2):
            for _ in range(len(LL1) - len(LL2)):
                temp_node = temp_node.next
                
        else:
            bigger_ll = LL1
            temp_node = LL2.head
            for _ in range(len(LL2) - len(LL1)):
                temp_node = temp_node.next
        
        # we now know which list is bigger and we move temp_node accordingly
        
        
        if bigger_ll == 1:
            current_node1 = temp_node
            current_node2 = LL2.head
        else:
            current_node2 = temp_node
            current_node1 = LL1.head
        
        while temp_node:
            if current_node1 == current_node2:
                return current_node1
            temp_node = temp_node.next
            current_node1 = current_node1.next
            current_node2 = current_node2.next

        else:
            return None

sol = Solution()

ll1 = LinkedList()
ll2 = LinkedList()

[ll1.add(i) for i in range(1,10)]
[ll2.add(i) for i in range(3,10)]

new_node = Node(15)

# adding node of same reference on both to check if method works or not
ll1.tail.next = new_node
ll1.tail = new_node
ll2.tail.next = new_node
ll2.tail = new_node
print(ll1)
print(ll2)
result = sol.intersection(ll1, ll2)
if result:
    print(result.value)