# Import the Queue class (assumed to be correctly implemented)
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue

class BinaryTree:
    def __init__(self, data = None) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def addChild(self, node):
        if not self.data:  # Assuming an empty node means no data
            self.data = node.data
        else:
            custom_queue = Queue()
            custom_queue.enqueue(self)
            while not custom_queue.isEmpty():
                root: BinaryTree = custom_queue.dequeue()

                if root.leftChild is not None:
                    custom_queue.enqueue(root.leftChild)
                else:
                    root.leftChild = node
                    return "Added Successfully"

                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)
                else:
                    root.rightChild = node
                    return "Added Successfully"

    def __str__(self) -> str:
        if not self.data:
            return "Empty Tree"
        else:
            tree = ""
            custom_queue = Queue()
            custom_queue.enqueue(self)

            while not custom_queue.isEmpty():
                root = custom_queue.dequeue()
                tree += str(root.data) + "\n"

                if root.leftChild is not None:
                    custom_queue.enqueue(root.leftChild)
                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)

            return tree

# Functions for deleting the deepest node

def getDeepestNode(root_node):
    if not root_node:
        return None

    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    last_node = None
    while not custom_queue.isEmpty():
        last_node = custom_queue.dequeue()
        if last_node.leftChild:
            custom_queue.enqueue(last_node.leftChild)
        if last_node.rightChild:
            custom_queue.enqueue(last_node.rightChild)

    return last_node

def deleteDeepestNode(root_node, deepest_node):
    if not root_node:
        return

    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.isEmpty():
        node = custom_queue.dequeue()

        if node is deepest_node:
            node = None
            return

        if node.leftChild:
            if node.leftChild is deepest_node:
                node.leftChild = None
                return
            else:
                custom_queue.enqueue(node.leftChild)

        if node.rightChild:
            if node.rightChild is deepest_node:
                node.rightChild = None
                return
            else:
                custom_queue.enqueue(node.rightChild)

# Testing the implementation
def test():
        
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

# Delete method for the the given node

def delete(root_node, node):
    """Return Successfully as string or None if failed
    First it found the node we want to delete then it find the last
    node in tree then it replaces the last node in tree with the out given node value
    and then delete the last node i.e set it to None"""
    
    if not root_node:
        return None
    
    else:
        # First we need to find the node location which we want to delete 
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.data == node:   # found the node we want to delete
                # lets found the last node of Binary Tree
                last_node = getDeepestNode(root_node)
                
                # setting the last to our target node which we want to delete
                root.data = last_node.data  # we did't change the child of target node here just the label
                
                # Now we will remove the last last node since it already been assign
                deleteDeepestNode(root_node, last_node)
                return "Delete Successfully"

            if root.leftChild:
                custom_queue.enqueue(root.leftChild)
            
            if root.rightChild:
                custom_queue.enqueue(root.rightChild)
        
        return "Failed to delete"
    
    
def deleteTree(rootnode) -> str:
    rootnode.data = None
    rootnode.leftChild = None
    rootnode.rightChild = None
    return "Deleted Successfully"


def test():
        
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
    print("Here we will delete\n")
    
    print(delete(newBT, "Hot"))

    print(newBT)
    
    print(deleteTree(newBT))
    print(newBT)
test()
