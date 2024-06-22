"""Here I will create Binary Heap
Binary Heap have 2 children or 0 children
and its leaf node only have 0 children
Here I will implement heap using List data type
root(index = 1), leftChild = (2n), rightChild = (2n + 1)
n is parent index"""

class Heap:
    def __init__(self, size = 2) -> None:
        self.max_size = size + 1
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0  # size of heap with actual elements

def peekOfHeap(root_node = None):
    if not root_node:
        return
    return root_node[1]

# size of heap function
def sizeOfHeap(root_node : None):
    if not root_node:
        return
    return root_node.heap_size


# print(sizeOfHeap(myheap))

def levelOrderTraversal(root_node : Heap | None = None) -> None:
    if not root_node or root_node.heap_size == 0:
        print("Empty Heap")
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])

# levelOrderTraversal(myheap)

def heapifyTreeInsert(root_node : Heap, index : int, heap_type : str) -> None:
    """Arrange and maintain the property of heap according to its heap_type
    work recursively and with index of leaf node"""
    parent_index = int(index / 2)
    
    if index <= 1:
        return
    
    elif heap_type.capitalize() == "Min":
        if root_node.custom_list[parent_index] > root_node.custom_list[index]:  # means parent is greater than child(needed to fix)
            temp = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = root_node.custom_list[index]
            root_node.custom_list[index] = temp
        # calling it recursively
        heapifyTreeInsert(root_node, parent_index, heap_type)
        
    elif heap_type.capitalize() == "Max":
        if root_node.custom_list[parent_index] < root_node.custom_list[index]:  # means parent is smaller than child(needed to fix)
            temp = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = root_node.custom_list[index]
            root_node.custom_list[index] = temp
        # calling it recursively
        heapifyTreeInsert(root_node, parent_index, heap_type)
        
def insertNode(root_node : Heap, value : int, heap_type : str = "Min"):
    if root_node.heap_size + 1 == root_node.max_size:
        return "Max size reached"
    root_node.custom_list[root_node.heap_size + 1] = value
    root_node.heap_size += 1
    heapifyTreeInsert(root_node, root_node.heap_size, heap_type)
    return "Value inserted Successfully"

# insertNode(myheap, 1)


# levelOrderTraversal(myheap)

def heapifyTreeExtract(root_node : Heap, index : int, heap_type : str = "Min"):
    left_index = 2 * index
    right_index = 2 * index + 1
    swap_child = 0
    
    # when only one node exits
    if left_index > root_node.heap_size:   # means heap have not more than one element
        return
    
    elif left_index == root_node.heap_size:  # means it have only one child i.e left Child(means 2 value in heap)
        if heap_type.capitalize() == "Min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:    # In min type heap parent is greater(needed to fix)
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return  

        else:   # for the Max type heap with only one child (means 2 value in heap)
            if root_node.custom_list[index] < root_node.custom_list[left_index]:    # In min type heap parent is greater(needed to fix)
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return 
    
    # Now case of 2 Children
    else:
        if heap_type.capitalize() == "Min":
            # now we need to find which child is min so we can compare it with parent
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            
            # type is Min type heap and parent is greater than its child so we need to fix it
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
        
        else:
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            
            # type is Min type heap and parent is greater than its child so we need to fix it
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp 
        
        # calling function recursively
        heapifyTreeExtract(root_node, swap_child, heap_type)
        
    
# now to create the extract node
def extractNode(root_node : Heap, heap_type : str = "Min"):
    if root_node.heap_size == 0:
        return None
    else:
        extracted_node = root_node.custom_list[1]
        # now to replace it value with last index in heap
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        
        # now to set last index in heap to None
        root_node.custom_list[root_node.heap_size] = None
        
        root_node.heap_size -= 1
        # now to call heapify extract method to fix the tree to heap properties
        heapifyTreeExtract(root_node, 1, heap_type)
        return extracted_node
    
    

myheap = Heap(4)

insertNode(myheap, 4, "Max")
insertNode(myheap, 5, "Max")
insertNode(myheap, 2, "Max")
insertNode(myheap, 1, "Max")

levelOrderTraversal(myheap)

print("After deleting")

print(extractNode(myheap, "Max"))
print("\n\n")
levelOrderTraversal(myheap)


def deleteAll(root_node):
    root_node.custom_list = None
    return "Heap Deleted Successfully"

