# Here I will use recursion do find the value of factorial

def factorial(num : int) -> int:
    assert num >= 0 and int(num) == num, "only positive integers are allowed"
    
    if num in [0, 1]:
        return 1
    
    return num * factorial(num -1)

print("Factorial of 5 : ",factorial(-1))