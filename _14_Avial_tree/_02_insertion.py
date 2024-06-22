from typing import Optional, Any
# Import the Queue class (assumed to be correctly implemented)
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue


class AvlTree:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def __str__(self) -> str:
        if self.data is None:
            return "Empty Binary Tree"
        else:
            mytree: str = ""
            custom_queue = Queue()
            custom_queue.enqueue(self)
            while not (custom_queue.isEmpty()):
                root = custom_queue.dequeue()
                mytree += str(root.data) + "\n"
                if root.leftChild is not None:
                    custom_queue.enqueue(root.leftChild)
                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)
            return mytree   

def getHeight(root_node) -> int:
    if not root_node:
        return 0
    return root_node.height

def rightRotation(disbalance_node: AvlTree) -> AvlTree:
    new_root: AvlTree = disbalance_node.leftChild
    disbalance_node.leftChild = new_root.rightChild
    new_root.rightChild = disbalance_node  # Corrected typo

    disbalance_node.height = 1 + max(getHeight(disbalance_node.leftChild), getHeight(disbalance_node.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))

    return new_root

def leftRotation(disbalance_node: AvlTree) -> AvlTree:
    new_root: AvlTree = disbalance_node.rightChild
    disbalance_node.rightChild = new_root.leftChild
    new_root.leftChild = disbalance_node

    disbalance_node.height = 1 + max(getHeight(disbalance_node.leftChild), getHeight(disbalance_node.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))
    return new_root

def getBalance(root_node: AvlTree) -> int:
    if not root_node:
        return 0
    return getHeight(root_node.leftChild) - getHeight(root_node.rightChild)

def insertNode(root_node: AvlTree, value: int) -> AvlTree:
    if not root_node:
        return AvlTree(value)
    
    # Perform the normal BST insert
    if value < root_node.data:
        root_node.leftChild = insertNode(root_node.leftChild, value)
    else:
        root_node.rightChild = insertNode(root_node.rightChild, value)
    
    # Update the height of this ancestor node
    root_node.height = 1 + max(getHeight(root_node.leftChild), getHeight(root_node.rightChild))
    
    # Get the balance factor
    balance = getBalance(root_node)
    
    # Check the balance factor and perform rotations if needed
    
    # Left Left Case
    if balance > 1 and value < root_node.leftChild.data:
        return rightRotation(root_node)
    
    # Left Right Case
    if balance > 1 and value > root_node.leftChild.data:
        root_node.leftChild = leftRotation(root_node.leftChild)
        return rightRotation(root_node)
    
    # Right Right Case
    if balance < -1 and value > root_node.rightChild.data:
        return leftRotation(root_node)
    
    # Right Left Case
    if balance < -1 and value < root_node.rightChild.data:
        root_node.rightChild = rightRotation(root_node.rightChild)
        return leftRotation(root_node)
    
    # Return the updated root node
    return root_node


# Testing the insertNode function
newAvl = AvlTree(5)
newAvl = insertNode(newAvl, 10)
newAvl = insertNode(newAvl, 15)
newAvl = insertNode(newAvl, 20)

print(newAvl)
