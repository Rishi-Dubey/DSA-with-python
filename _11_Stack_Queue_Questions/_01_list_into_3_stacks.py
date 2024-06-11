"""Program that will divide a single list into 3 stack
means use only a single list for three stacks
"""


class MultiStack:
    def __init__(self, stack_size) -> None:
        # size of each stack(each one of 3)
        self.stack_size = stack_size

        # no of stacks we want
        self.number_stacks: int = 3

        # init a cust list with 0s:
        self.cust_list: list = [0] * (stack_size * self.number_stacks)

        # store how much fill the each stacks are (stack(0) if == stack_size means full)
        self.sizes: list = self.number_stacks * [0]     # will store the len of each stack
    
    def isFull(self, stack_no) -> bool:
        if self.sizes[stack_no] == self.stack_size:
            return True
        else:
            return False

    def isEmpty(self, stack_no):
        if self.sizes[stack_no] == 0:
            return True
        else : return False
    
    def indexOfTop(self, stack_no):
        """Return the top elements index of given stack no
        means return the last added elements index in given stack_no"""
        offset : int = stack_no * self.stack_size   # well count all the element before the given_stack
        return offset + self.sizes[stack_no] - 1 # added that stacks size minus 1 for exact index

    def push(self, stack_no, value):
        """Adds element in given stack_no return None"""
        if self.isFull(stack_no):
            print("!!!Overflow")
        else:
            self.sizes[stack_no] += 1  # we update the size now so top also update(which we will change)
            self.cust_list[self.indexOfTop(stack_no)] = value
            
    def pop(self, stack_no):
        if self.isEmpty():
            print("!!! Underflow")
        else:
            value = self.cust_list[self.indexOfTop((stack_no))]
            self.cust_list[self.indexOfTop(stack_no)] = 0
            self.sizes[stack_no] -= 1
            return value
    
    def peek(self, stack_no):
        if self.isEmpty(stack_no):
            return None
        else:
            return self.cust_list[self.indexOfTop(stack_no)]
        
    def __str__(self) -> str:
        value = [str(i) for i in self.cust_list]
        if value == "":
            return "Empty Stack"
        else:
            return ",".join(value)    
c = MultiStack(3)

print(c.isFull(0))
print(c.push(0,1))
print(c.push(0,2))
print(c.push(0,3))
print(c.push(1,4))
print(c.push(1,5))
print(c.push(1,6))
print(c.push(2,7))
print(c.peek(0))

print(c)