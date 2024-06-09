"""Will create stack But with upper size limit
It will be implemented with list also"""

# stack -> LIFO -> Last in First Out
# Here I will implement stack using List
# Adv -> Easy to use , Ddv -> Slow as size grows


class Stack:
    def __init__(self, upper_limit) -> None:
        self.list = []
        self.upper_limit = upper_limit

    def __str__(self) -> str:
        if self.list == []:
            return "Empty Stack"
        
        mylist: list = [f"{i}" for i in reversed(self.list)]
        mystack = "\n".join(mylist)
        return mystack

    def isEmpty(self) -> bool:
        """Return True if Stack is empty else False"""
        if self.list == []:
            return True
        return False

    def isFull(self) -> bool:
        """Return True if Stack is full else False"""
        if self.upper_limit == len(self.list):
            return True
        return False

    def push(self, value) -> None:
        """push value into the stack
        return the overflow error if stack if full
        else None"""
        if self.isFull():
            print("Overflow !!!")
        else:
            self.list.append(value)
            print("Value added successfully")

    def pop(self) -> None | int:
        """Remove the last one first(LIFO)
        return underflow error if the stack is empty"""
        if self.isEmpty():
            print("Underflow")
            return None

        return self.list.pop()

    def peek(self) -> int | None:
        """Return the last element in the stack or None if stack is empty"""
        if self.list == []:
            print("Empty Stack")
            return None
        else:
            self.list[-1]

    def delete(self) -> None:
        """Delete the entire stack return None"""
        self.list = None
        print("Stack Deleted Successfully")

stack: Stack = Stack(5)
print(stack.isFull())
[stack.push(i) for i in range(5)]
stack.push(10)
print(stack)