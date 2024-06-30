def partition(customList : list, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i + 1], customList[high] = customList[high], customList[i + 1]
    return i + 1

def quickSort(customList : list, low,  high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi -1)
        quickSort(customList, pi+1, high)
        
array = [10, 11, 4, 6, 2, 8]
quickSort(array, 0, 5)
print(array)