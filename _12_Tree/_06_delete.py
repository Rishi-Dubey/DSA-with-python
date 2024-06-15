"""Here I will create insert method for the Binary Tree
It will use Level order traversal i.e it uses Queue which is faster than stack"""

import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue

class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def addChild(self, node):
        if not self.data:
            self.data = node.data
        else:
            custom_queue = Queue()
            custom_queue.enqueue(self)
            while not custom_queue.isEmpty():
                root: BinaryTree = custom_queue.dequeue()

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
        if not self.data:
            return "Empty Tree"
        else:
            tree: str = ""
            custom_queue: Queue = Queue()
            custom_queue.enqueue(self)
            
            while custom_queue.isEmpty() is False:
                root = custom_queue.dequeue()
                tree += root.data + "\n"
                
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



# Here In separate from the class I will create Delete method
def getDeepestNode(root_node):
    if not root_node:
        return None

    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.isEmpty():
            root: BinaryTree = custom_queue.dequeue()
            if root.leftChild is not None:
                custom_queue.enqueue(root.leftChild)
            if root.rightChild is not None:
                custom_queue.enqueue(root.rightChild)

        return root
    

def deleteDeepestNode(root_node, deepest_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.isEmpty():
            root : BinaryTree = custom_queue.dequeue()
            
            # checking if the root is deepest node or not
            if root is deepest_node:
                root = None
                return
            
            #else we will check it's left and right child
            if root.leftChild:
                if root.leftChild is deepest_node:
                    root.leftChild = None
                    return
                else:
                    custom_queue.enqueue(root.leftChild)
            
            if root.rightChild:
                if root.rightChild is deepest_node:
                    root.rightChild = None
                    return
                else:
                    custom_queue.enqueue(root.rightChild)
            

dn = getDeepestNode(newBT)
print(dn)

deleteDeepestNode(newBT, deepest_node = dn)

print(newBT)