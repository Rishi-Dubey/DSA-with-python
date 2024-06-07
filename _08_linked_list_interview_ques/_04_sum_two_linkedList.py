"""Goal ->  When a two linked list which consists of numbers
            Numbers in each node is single digit combine all nodes makes the exact number
            1->2->3 so 123
            
            we have to add both LinkedList and give out a new linked list
            LL1 = [4, 2, 6]
            ll2 = [3, 8, 5]
            
            so 624 + 583 = 1207
            so return new_linked_list = 7->0->2->1
            yes values add is like reverse order
            """

from LinkedList import LinkedList as LL


def Solution(ll1: LL, ll2: LL):
    """Return the Linkedlist which is sum of LL1 and LL2
    and none if both LL1 and LL2 is None"""

    sumlinkedlist: LL = LL()  # get an empty linked List which will store the sum

    if ll1.head is None and ll2.head is None:
        print("Both Linked List is Empty")
        return sumlinkedlist

    temp_node1 = ll1.head   # will use to traverse through temp_node1
    temp_node2 = ll2.head   # will use to traverse through temp_node2

    list1: list = []  # will store the values of ll1
    list2: list = []  # will store the values of ll2

    while temp_node1:
        list1.append(temp_node1.value)
        temp_node1 = temp_node1.next
    while temp_node2:
        list2.append(temp_node2.value)
        temp_node2 = temp_node2.next

    # now we have node values of ll1 and ll2 linkedlist class in out list1 and list2
    # we will now combine the sum of both list1 and list2
    sum_list: list = []

    # assume
    small_len_list = len(list1)
    big_len_list = len(list2)

    if len(list1) >= len(list2):
        big_len_list = len(list1)
        small_len_list = len(list2)

    extra = 0
    for i in range(big_len_list):
        if i < small_len_list:
            sum = list1[i] + list2[i] + extra
            ones = sum % 10
            tens = sum // 10
            sum_list.append(ones)
            extra = tens

        else:
            sum = list1[i] + extra
            ones = sum % 10
            tens = sum // 10
            sum_list.append(ones)
            extra = tens

    if extra != 0:
        sum_list.append(extra)

    for i in sum_list:
        sumlinkedlist.add(i)
    return sumlinkedlist


LL1 = LL()
LL2 = LL()

LL1.add(7)
LL1.add(1)
LL1.add(6)
LL2.add(5)
LL2.add(9)
LL2.add(2)

sol = Solution(LL1, LL2)
print(sol)
