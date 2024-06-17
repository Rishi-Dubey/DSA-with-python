"""Here I will create Binary Search Tree
It is subset of binary tree here left child is always smaller or equal to root
and rightChild is always greater than root.
I will implement using Linked List"""

from typing import Optional, Any
# Import the Queue class (assumed to be correctly implemented)
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue


class BinarySearchTree:
    def __init__(self, data=None) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

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

def insertNode(root_node: BinarySearchTree, data: Optional[Any]) -> str:
    """Return an Successfully message in str 
    Insert the data in given root node accordingly
    use's recursion"""

    if root_node.data is None:  # means root node itself is empty so we will insert to rootnode
        root_node.data = data
        print("Value Inserted Successfully")

    elif data <= root_node.data:   # for the leftChild when data <= root
        if root_node.leftChild is None:
            root_node.leftChild = BinarySearchTree(data)
            return "Value Inserted Successfully"
        else:
            # we call function recursively until it find the right place
            insertNode(root_node.leftChild, data)

    else:  # means add it to right child
        if root_node.rightChild is None:   # we find the place to insert
            root_node.rightChild = BinarySearchTree(data)
            return "Value Inserted Successfully"
        else:
            # we call the function recursively until we find the right place in Right child of the root
            insertNode(root_node.rightChild, data)


newBST = BinarySearchTree(70)
# insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)


def preOrderTraversal(root_node):
    """only print the value
    root -> left subtree -> right subtree
    """
    if not root_node:
        return
    else:
        print(root_node.data)
        preOrderTraversal(root_node.leftChild)
        preOrderTraversal(root_node.rightChild)

# preOrderTraversal(newBST)  

def inOrderTraversal(root_node):
    if not root_node:
        return
    else:
        inOrderTraversal(root_node.leftChild)   # until we reach where child becomes None we will get the return
        print(root_node.data)
        inOrderTraversal(root_node.rightChild)

# inOrderTraversal(newBST)

def postOrderTraversal(root_node):
    if not root_node:
        return
    else:
        postOrderTraversal(root_node.leftChild)
        postOrderTraversal(root_node.rightChild)
        print(root_node.data)

# postOrderTraversal(newBST)
print(newBST.leftChild.leftChild)
print(newBST)