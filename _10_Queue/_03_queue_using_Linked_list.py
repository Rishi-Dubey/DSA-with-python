"""Here I will implement all the methods of Queue using Linked List"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> int:
        if self.head is None:
            return None

        else:
            item = self.head.value
            if self.head.next is None:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
            return item

    def __str__(self) -> str:
        if self.head is None:
            return "Empty Queue"

        else:
            queue = []
            current_node = self.head
            while current_node:
                queue.append(str(current_node.value))
                current_node = current_node.next

            return " -> ".join(queue)

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def peek(self) -> int | None:
        if self.isEmpty():
            return None
        else:
            return self.head.value


myqueue = Queue()

print(myqueue.isEmpty())
print(myqueue.dequeue())
print(myqueue)
myqueue.dequeue()

print("=============================")

myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)

print(myqueue)
print(myqueue.dequeue())
print(myqueue)
