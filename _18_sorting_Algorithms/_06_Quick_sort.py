def partition(array : list, initial_index : int, final_index : int):
    pivot = array[final_index]  # value of final index
    
    i = initial_index
    for j in range(initial_index, final_index):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[final_index] = array[final_index], array[i]
    return i

array = [10, 3, 4, 2, 8]

def quickSort(array : list, initial_index, final_index):
    if initial_index < final_index:
        sorted_index = partition(array, initial_index, final_index)
    
        # well now we know we have sorted the sorted_index in partition function
        # now we will sort the value to its left and to its right
        # print(f"II : {initial_index}, FI : {final_index}, TI : {sorted_index}")
        quickSort(array, initial_index, sorted_index - 1)   # means value just before the sorted index
        quickSort(array, sorted_index + 1, final_index)  # means value just after the sorted index
        
quickSort(array, 0, 4)
print(array)