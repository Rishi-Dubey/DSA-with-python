"""Here I will use the Bubble Sort Algorithm to sort an list
Bubble sort -> Compare Adjacent element and swap them accordingly till ends
then last element in list become sorted so no need to check it. then repeat the process again."""


def bubbleSort(array : list | None = None) -> None | list[input]:
    """Return the list in Ascending order"""
    
    if array is None or len(array) in (0, 1):
        return array
    else:
        for i in range(len(array) - 1):    # repeat since we don't need to check (index 0) we exclude it
            for j in range(len(array) - 1 - i):    # minus 1 since we use(j + 1) and i since know last element 
                # in every iteration will be in right position means sorted
                if array[j] > array[j + 1]:     # not follow ascending order
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    
print(bubbleSort())