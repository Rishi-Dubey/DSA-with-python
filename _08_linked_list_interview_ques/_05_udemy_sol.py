"""Program will find the intersection points of two linked list and return 
the intersection node.
Note -> Intersection is compared by node reference not the value"""

from LinkedList import LinkedList, Node

class Solution(LinkedList):
    def __init__(self) -> None:
        super().__init__()
    
    def intersection(self, LL1: LinkedList, LL2: LinkedList):
        if ll2.tail != ll1.tail:    # if we found intersection means we have all the element same
            return None             # down to the last element so both their tails must be same
                                    
        bigger : LinkedList  = LL1 if len(LL1) > len(LL2) else LL2
        smaller : LinkedList = LL1 if len(LL1) < len(LL2) else LL2
        
        diff : int = len(bigger) - len(smaller)
        bigger = bigger.head
        smaller = smaller.head
        for i in range(diff):
            bigger = bigger.next
        
        # now bigger is starting from the point where its len will be same as smaller
        while bigger is not smaller:    # means there value are not same
            bigger = bigger.next
            smaller = smaller.next
        
        return bigger.value

    # program to help
    def add_same_value(self, ll1 : LinkedList, ll2 : LinkedList, value):
        # adding the same reference value in both
        new_node = Node(value)
        ll1.tail.next = new_node
        ll1.tail = new_node
        ll2.tail.next = new_node
        ll2.tail = new_node
    
sol = Solution()
ll1 = LinkedList()
ll2 = LinkedList()

[ll1.add(i) for i in range(1, 10)]
[ll2.add(i) for i in range(5, 7)]

[sol.add_same_value(ll1, ll2, i) for i in range(14, 20)]

print(ll1)
print(ll2)

result = sol.intersection(ll1, ll2)
if result is not None:
    print(f"Intersection point value : {result}")