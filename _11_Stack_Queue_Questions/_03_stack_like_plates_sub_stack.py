"""Implement stack like the plates
when a certain capacity exceeds it create new sub stack
all the method should work as it is a single stack

-> new method : popAt -> takes index of given sub stack at perform pop"""

class PlateStack:
    def __init__(self, capacity = 1) -> None:
        self.capacity = capacity
        self.stacks = []    # creates an nested list
        
    def __str__(self) -> list:
        return str(self.stacks)
    
    def push(self, value):
        if len(self.stacks) > 0 and (len(self.stacks[-1]) < self.capacity):
            self.stacks[-1].append(value)   # goes to nested list
        
        else:
            self.stacks.append([value]) # adding as an list inside the list
        
    def pop(self):
        # while loop remove the empty list inside the list if the last it that
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    
    def popAt(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

cs = PlateStack(capacity=2)

cs.push(1)
cs.push(2)
cs.push(3)
print(cs)
print(cs.pop())
print(cs.pop())
print(cs)