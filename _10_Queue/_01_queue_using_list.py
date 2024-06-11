"""Queue stands for FIFO -> First In First Out
Here I will implement Queue and all its method using list
"""


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value) -> None:
        """Return None
        Add the given value to queue"""
        self.queue.append(value)

    def dequeue(self) -> int | None:
        """Return the first element that got dequeue or None if queue is empty"""
        if self.isEmpty():
            print("!!! Empty Queue ):")
        else:
            return self.queue.pop(0)

    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

    def peek(self) -> int | None:
        if self.isEmpty():
            print("!!!Empty Queue ):\n")
        else:
            return self.queue[0]

    def __str__(self) -> str:
        if self.isEmpty():
            return "!!! Empty Queue"
        else:
            myqueue = [str(i) for i in self.queue]
            return " ".join(myqueue)
    
    def delete(self) -> None:
        self.queue = []

myqueue = Queue()
print(myqueue)
[myqueue.enqueue(i) for i in range(5)]
print(myqueue)

print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
