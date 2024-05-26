"""Fib -> 0, 1, 1, 2, 3
   fib(n) -> fib(n-1) + fib(n-2)"""
   
from functools import lru_cache   
   
@lru_cache(maxsize= None)   
def fibonacci_series(index : int) -> int:
    assert index >= 0 and index == int(index), "Only Zero positive integer is allowed"
    
    if (index == 0):
        return 0

    elif (index in [1, 2]):
        return 1

    return fibonacci_series(index - 1) + fibonacci_series(index - 2)


result : int = fibonacci_series(100)
print("Result : ",result)