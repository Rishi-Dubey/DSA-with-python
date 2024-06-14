"""Here I will use all the traversal methods
1) Pre Order Traversal -> first visit all lefts then right nodes
2) InOrder Traversal -> First left subtree then its parent then its 
right sibling then again repeat this process
3) PostOrder Traversal -> First left Subtree , Right subtree, root of subtree repeat... then main root
4) Level Order Traversal -> Root then left child of root , right child ... repeat
"""
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue


class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.rightChild = None
        self.leftChild = None


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

# now creating PreOrder Traversal Class to traverse through the all Binary Tree


class PreOrderTraversal:
    def __init__(self, root_node: BinaryTree) -> None:
        self.rootnode = root_node
        if not self.rootnode:
            return
        else:
            print(root_node.data)
            PreOrderTraversal(root_node.leftChild)
            PreOrderTraversal(root_node.rightChild)


# newTraversal= PreOrderTraversal(newBT)
print("___________________")
# now creating InOrder Traversal Class


class InOrderTraversal:
    def __init__(self, root_node: BinaryTree) -> None:
        if not root_node:
            return
        else:
            InOrderTraversal(root_node.leftChild)
            print(root_node.data)
            InOrderTraversal(root_node.rightChild)

# new_Tra = InOrderTraversal(newBT)


# now creating Post order traversal
class PostOrderTraversal:
    def __init__(self, rootnode: BinaryTree) -> None:
        if not rootnode:
            return
        else:
            PostOrderTraversal(rootnode.leftChild)
            PostOrderTraversal(rootnode.rightChild)
            print(rootnode.data)

# newTra = PostOrderTraversal(newBT)


# now creating Level order traversal
class LevelOrderTraversal:
    def __init__(self, root_node: BinaryTree) -> None:
        if not root_node:
            return
        else:
            custom_queue: Queue = Queue()
            custom_queue.enqueue(root_node)

            while custom_queue.isEmpty() is False:
                root = custom_queue.dequeue()
                print(root.data)

                if root.leftChild is not None:
                    custom_queue.enqueue(root.leftChild)

                if root.rightChild is not None:
                    custom_queue.enqueue(root.rightChild)


newTra = LevelOrderTraversal(newBT)
