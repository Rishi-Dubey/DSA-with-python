"""Here I will create binary Tree
Binary Tree -> Tree only consists of not more than 2 node(utmost 2 nodes)"""

class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


mytree = BinaryNode("Fast Food")