"""Here I will solve the same sum_problem but with different way"""
from LinkedList import LinkedList as ll

def solution(l1 : ll, l2: ll):
    n1 = l1.head
    n2 = l2.head
    
    sum_linked_list = ll()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        sum_linked_list.add(result % 10)    # adding the ones digit
        carry = result // 10
        
    if carry != 0:
        sum_linked_list.add(carry)
    return sum_linked_list
    
LL1 = ll()
LL2 = ll()

LL1.add(7)
LL1.add(1)
LL1.add(6)
LL2.add(5)
LL2.add(9)
LL2.add(2)

sol = solution(LL1, LL2)
print(sol)
            
