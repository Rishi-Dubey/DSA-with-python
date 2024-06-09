"""Here I will implement Stack using Linked list
with all the operation or methods of stack"""


class Item:
    def __init__(self, Value) -> None:
        self.value = Value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        if self.head is None:
            return 0
        current_node = self.head
        len = 0
        while current_node:
            len += 1
            current_node = current_node.next
        return len

    def push(self, value) -> None:
        new_item = Item(value)
        if self.head is None:
            self.head = new_item

        else:
            new_item.next = self.head
            self.head = new_item

    def __str__(self) -> str:
        if self.head is None:
            return ("Empty Stack")

        else:
            current_node = self.head
            mystack = ""
            while current_node:
                mystack = mystack + str(current_node.value) + "\n"
                current_node = current_node.next

            return mystack

    def pop(self) -> int | None:
        if self.head is None:
            print("!!! Underflow")
            return None
        else:
            item_deleted = self.head.value  # item we will delete
            self.head = self.head.next
            return item_deleted

    def peek(self) -> None | int:
        if self.head is None:
            print("Empty Stack")
            return None
        else:
            return self.head.value

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def delete(self) -> None:
        self.head = None
        print("Stack deleted successfully")


mystack = Stack()
print(len(mystack))
[mystack.push(i) for i in range(4)]
print(mystack)

mystack.pop()
print(mystack)

print(mystack.peek())
print(mystack.isEmpty())
print(len(mystack))