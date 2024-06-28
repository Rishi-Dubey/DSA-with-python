"""Here I will implement Insertion Sort Function
Insertion Sort -> Moves element to sorted side and then sort them there
means it moves element one by one to sorted side and place them there accordingly
"""

def insertionSort(array : list | None = None) -> None:
    """Return the list in Ascending order"""
    
    if array is None or len(array) in (0, 1):
        return array
    
    else:
        for i in range(1, len(array)):
            key = array[i]  # storing the value since it going to be replaced
            j = i - 1       # index we will use for comparison
            while j >= 0 and key < array[j]:    # if we found any value which is bigger than key we move the
                # value to key position and key position will be lost now we have two same value
                # at index j and j + 1. we will repeat this step until upper condition become false
                array[j + 1] = array[j]
                j -= 1
                
            # adding the key value to its right place
            array[j + 1] = key
        return array
    
print(insertionSort([10, 3, 4, 6, 2, 1]))