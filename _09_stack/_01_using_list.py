# stack -> LIFO -> Last in First Out
# Here I will implement stack using List
# Adv -> Easy to use , Ddv -> Slow as size grows

class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def __str__(self) -> str:
        mylist : list = [f"{i}" for i in reversed(self.list)]
        mystack = "\n".join(mylist)
        return mystack
    
    def isEmpty(self) -> bool:
        """Return True if Stack is empty else False"""
        if self.list == []:
            return True
        return False
    
    def push(self, value) -> None:
        """push value into the stack
        return the overflow error if stack if full
        else None"""
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
stack = Stack()
print(stack.isEmpty())

stack.pop()
stack.peek()