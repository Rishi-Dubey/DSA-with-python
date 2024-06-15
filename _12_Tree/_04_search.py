"""Here I will create search method for the Binary Tree
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

    def addChildLeft(self, tree):
        self.leftChild = tree
    
    def addChildRight(self, tree):
        self.rightChild = tree

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

# adding to leftchild and rightchild
leftChild.leftChild = Coffee
leftChild.rightChild = Chai

rightChild.rightChild = fruti
rightChild.leftChild = Coca_Cola

# adding it to newBt
newBT.leftChild = leftChild
newBT.rightChild = rightChild

print(newBT)

print(newBT.search("Fruti"))