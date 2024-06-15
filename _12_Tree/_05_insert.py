"""Here I will create insert method for the Binary Tree
It will use Level order traversal i.e it uses Queue which is faster than stack"""
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue


class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def search(self, data):
        """Return Node or None
         for the search -> Using Level order traversal"""
        if not self.leftChild:
            return
        
        custom_queue : Queue = Queue()
        custom_queue.enqueue(self)
        
        while not custom_queue.isEmpty():    # means run till it becomes empty
            root : BinaryTree = custom_queue.dequeue()   # will store the root of three first
            if data == root.data:
                return root
             
            if root.leftChild is not None:
                custom_queue.enqueue(root.leftChild)  
            if root.rightChild is not None:
                custom_queue.enqueue(root.rightChild)

    def addChild(self, node):
        if not self:
            self = node
        else:
            custom_queue = Queue()
            custom_queue.enqueue(self)
            while not custom_queue.isEmpty():
                root : BinaryTree = custom_queue.dequeue()

                # Now we will check if left child exits or not if exits add it to queue
                # and if not exits we will add node to leftchild
                if root.leftChild is not None:  # if it already exits no need to add value here
                    custom_queue.enqueue(root.leftChild)

                else:   # if left child not exits we will add node to left child of main root
                    root.leftChild = node
                    return "Added Successfully"
                # now we check the right child
                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)
                else: 
                    root.rightChild = node
                    return "Added Successfully"               

    def __str__(self) -> str:
        if not self:
            return
        else:
            tree : str = ""
            custom_queue: Queue = Queue()
            custom_queue.enqueue(self)
            level = 0
            while custom_queue.isEmpty() is False:
                root = custom_queue.dequeue()
                tree += root.data + "\n"
                level += 1
                if root.leftChild is not None:
                    custom_queue.enqueue(root.leftChild)

                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)
                   
            return tree
        
newBT = BinaryTree("Drinks")

leftChild = BinaryTree("Hot")
Coffee = BinaryTree("Coffee")
Chai = BinaryTree("Chai")

rightChild = BinaryTree("Cold")
fruti = BinaryTree("Fruti")
Coca_Cola = BinaryTree("Coca_Cola")

# adding trees accordingly
newBT.addChild(leftChild)
newBT.addChild(rightChild)

leftChild.addChild(Coffee)
leftChild.addChild(Chai)

rightChild.addChild(fruti)
rightChild.addChild(Coca_Cola)

print(newBT)