"""Here I will create Binary Tree using list"""
from typing import Optional, Any
# Import the Queue class (assumed to be correctly implemented)
import sys
import os

# Add the directory containing your module to sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '_10_Queue')))

# Now you can import the module
from _03_queue_using_Linked_list import Queue


class BinaryTree:
    def __init__(self, size) -> None:
        self.max_size = size + 1
        self.tree : list = (size + 1) * [None]
        self.last_used_index = 0

    def insertNode(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "Full Binary Tree"
        else:
            self.last_used_index += 1
            self.tree[self.last_used_index] = value
            return "Value inserted Successfully"
        
    def __str__(self) -> str:
        if self.last_used_index == 0:
            return "Empty Binary Tree"
        else:
            try:
                return "\n".join([i for i in self.tree[1 : self.last_used_index + 1] if i != None])
            except:
                return "!!! Error Binary Tree don't exits"

    def search(self, value):
        if value in self.tree[1 : self.last_used_index + 1]:
            return "Value found"
        return "No found"
    
    # All types of traversal in Binary Tree using list
    def preOrderTraversal(self, index = 1):
        """Return None 
        Only print the Binary tree in
        Pre Order Traversal -> Root -> left Subtree -> Right Subtree
        """
        if index > self.last_used_index:
            return
        else:
            print(self.tree[index])
            self.preOrderTraversal(index * 2)   # calling left child recursively
            self.preOrderTraversal(index * 2 + 1) # calling right child recursively
    
    def postOrderTraversal(self, index = 1):
        """Return None
        Only print the Binary tree using
        Post Order Traversal -> Left subtree -> Right subtree -> root node"""

        if index > self.last_used_index:
            return
        else:
            self.postOrderTraversal(index * 2)
            self.postOrderTraversal(index * 2 + 1)
            print(self.tree[index])
    
    def levelOrderTraversal(self, index = 1):
        if self.last_used_index == 0:
            return "Empty Binary tree"
        for i in self.tree[1 : ]:
            print(f"{i}")
                
    def deleteNode(self, value = None) -> Optional[any]:
        """Return the delete node value or None in case when node don't exits or empty Binary tree"""
        if self.last_used_index == 0 or value is None:
            return "No node to delete"
        else:
            for i in range(1, self.last_used_index + 1):
                if self.tree[i] == value:
                    delete_value = value
                    self.tree[i] = self.tree[self.last_used_index]
                    self.tree[self.last_used_index] = None
                    self.last_used_index -= 1
                    return delete_value
            else:
                return "No such value exits"   
      
    def deleteAll(self) -> None:
        self.tree = None
        self.last_used_index = None
        
new_Bt = BinaryTree(size= 8)
# print(new_Bt)

new_Bt.insertNode("Drinks")
new_Bt.insertNode("Hot")
new_Bt.insertNode("Cold")
new_Bt.insertNode("Coffee")
new_Bt.insertNode("Chai")
new_Bt.insertNode("CocaCola")
new_Bt.insertNode("Fruti")
new_Bt.insertNode("Lol")
# print(new_Bt.insertNode("Lol221"))

# print(new_Bt)
# # print(new_Bt)
# print(new_Bt.search("Chai"))
# print()
# new_Bt.preOrderTraversal()
# new_Bt.postOrderTraversal()
# new_Bt.LevelOrderTraversal()
print(new_Bt.deleteNode("Coffee"))
print()
print(new_Bt)

new_Bt.deleteAll()

print(new_Bt)