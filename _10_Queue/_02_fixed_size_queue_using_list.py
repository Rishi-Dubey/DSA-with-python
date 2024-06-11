"""Here I will implement Queue using the list but it will have fixed size to make program faster"""


class Queue:
    def __init__(self, max_size) -> None:
        self.items: list = max_size * [None]
        self.start = -1     # index of first added element
        self.top = -1       # index of last added element
        self.max_size = max_size

    def __str__(self) -> str:
        return " ".join([str(i)  for i in self.items if i != None])

    def isFull(self):
        # check if top is just behind means no cell empty
        if (self.top + 1 == self.start):
            return True

        # check if start 0 and top is at last index
        elif (self.start == 0 and self.top == self.max_size - 1):
            return True

        else:
            return False

    def isEmpty(self):
        if self.start == -1 and self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return "Full Queue !!!"

        else:
            # means some index's at beginning is empty(but top is at last index)
            if self.top == self.max_size - 1:
                self.top = 0

            else:
                # if user first time insert value(only then start change)
                if self.start == -1:
                    self.start = 0

                self.top += 1        # top changes for every new value
            self.items[self.top] = value
            return "Value is added in Queue Successfully"

    def dequeue(self) -> int | None:
        if self.isEmpty():
            print("Empty Queue")
            return None
        else:
            item : int = self.items[self.start]   # first added item will be removed
            self.items[self.start] = None

            if self.start == self.top:  # means only one item exits
                self.top = -1
                self.start = -1
            elif self.start + 1 == self.max_size:   # when first added element is at last index and Queue is not empty
                self.start = 0    # goes to index (1)
            else:
                self.start += 1
            return item

    def peek(self):
        if self.isEmpty():
            print("Empty Queue ):")
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1
           
myqueue = Queue(3)
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue)
print(myqueue.dequeue())
# print(myqueue.dequeue())
print(myqueue)
print(myqueue.peek())