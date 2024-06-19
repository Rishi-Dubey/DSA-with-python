"""Program to delete node in Binary search Tree
1) If node is leaf node -> means last node of the binary tree
2) If node has one child then child will replace the parent node and parent node will be deleted
3) If node has two child then we will find the smallest node in right subtree and then it will
replace it and we delete the target node"""


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
        
    def preOrderTraversal(self):
        """PreOrder traversal (root, left, right)."""
        if self is None:
            return None
        print(self.data, end=" ")
        if self.leftChild:  
            self.leftChild.preOrderTraversal()  # now self -> self.leftChild
        if self.rightChild:
            self.rightChild.preOrderTraversal()


def insertNode(root_node: BinarySearchTree, data: int) -> str:
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
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

def minNodeValue(root_node : BinarySearchTree):
    current_node = root_node
    while current_node.leftChild is not None:
        current_node = current_node.leftChild
    return current_node


def deleteNode(root_node : BinarySearchTree, node_value : int):

    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.leftChild = deleteNode(root_node.leftChild, node_value)
    elif node_value > root_node.data:
        root_node.rightChild = deleteNode(root_node.rightChild, node_value)
    else:
        if root_node.leftChild is None:
            temp = root_node.rightChild
            root_node = None
            return temp
        
        if root_node.rightChild is None:
            temp = root_node.leftChild
            root_node = None
            return temp

        temp = minNodeValue(root_node.rightChild)
        root_node.data = temp.data
        root_node.rightChild = deleteNode(root_node.rightChild, temp.data)
    return root_node