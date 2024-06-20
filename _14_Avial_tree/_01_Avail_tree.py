"""Avail tree is same as Binary search tree but here we need the tree to be balanced
means the height of leftChild and rightChild should not be more than one
use -> It make the tree even faster also its operations"""


class AvlTree:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = None


newAvl = AvlTree(10)


def search(root_node, value):
    if not root_node:
        return False
    else:
        if root_node.data == value:
            print("Found at Main Root")
            return True

        elif value < root_node.data:
            if root_node.leftChild and root_node.leftChild.data == value:
                print("Found at left Subtree")
                return True
            else:
                search(root_node.leftChild, value)

        elif value > root_node.data:
            if root_node.rightChild and root_node.rightChild.data == value:
                print("Found at right Subtree")
                return True
            else:
                search(root_node.rightChild, value)
        return False        

print(search(newAvl, 10))