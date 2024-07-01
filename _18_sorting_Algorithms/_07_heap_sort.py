
def heapify(array : list, size, target_index):
    smallest = target_index     # assuming the smallest is target index
    leftChild = smallest * 2 + 1
    rightChild = smallest * 2 + 1
    
    if leftChild < size and array[leftChild] < array[smallest]:
        smallest = leftChild
    elif rightChild < size and array[rightChild] < array[smallest]:
        smallest = rightChild
    
    if smallest != target_index:
        # means we need to swap to parent to its smallest element
        array[target_index], array[smallest] = array[smallest], array[target_index]
        
        # since we change the heap we need to check again
        heapify(array, size, smallest)

def heapSort(array : list):
    size = len(array)
    
    # we are calling the heapify to convert our array into min heap
    # to avoid unnecessary call we will call only non leaf subtree nodes(nodes with children)
    for i in range(int(size / 2) -1, -1, -1):   # two child so size/2 and for index remove (-1)
        heapify(array, size, i)
    
    # Now we now our array is heapify to min heap
    # we just need to extract the first element of heap and again heapify it
    for i in range(size -1 , 0, -1):    # i (last index -> index(1))
        array[i], array[0] = array[0], array[i]     # swaping last with first element
        
        # Now after swaping the first index element(smallest in array) with last index element
        # we will call heapify with size reduce by 1
        # here heapify is getting call form 0 index since we just swapped the root index
        heapify(array, i, 0)
    
    
array = [10, 3, 4, 2, 8]
heapSort(array)
print(array)