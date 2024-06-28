"""Here I will implement Selection Sort Algorithm
Selection Sort Algorithm -> first found the smallest or biggest element in list then place it in index 0
then another smallest place it in index 1 ... making it sorted array"""

def selectionSort(array : list|None = None):
    """Return the array in Ascending Order"""
    if array is None or len(array) in (0, 1):
        return array
    else:
        for i in range(len(array) - 1):
            smallest_index = i
            for j in range(i + 1, len(array)):
                if array[smallest_index] > array[j]:
                    smallest_index = j
            
            # After finding the smallest value we swap it (Move it to sorted side)
            array[i], array[smallest_index] = array[smallest_index], array[i]
        return array

print(selectionSort([10, 4, 2, 8, 7, 3, 1]))