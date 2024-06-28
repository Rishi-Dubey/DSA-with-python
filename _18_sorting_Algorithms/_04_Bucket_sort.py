"""Here I will learn how to do Bucket Sort
Bucket sort first divides the array in n buckets
No of Buckets(n) = sqrt(len(array))
index of each element = ceil(i(element) * n(No of buckets) / max(array))

now we place the value in buckets according to their index
after that we sort the buckets -> Merge and return buckets combined list"""

from math import sqrt, ceil
from _01_Bubble_sort import bubbleSort

def bucketSort(array : list | None = None) -> list | None:
    """Using Bucket Sort return the unsorted array in Ascending Order"""
    
    if array is None or len(array) in (0, 1):
        return array
    else:
        num_of_buckets = round(sqrt(len(array)))
        
        custom_array = []
        # Now we know the no of buckets we will create them
        for _ in range(num_of_buckets):
            custom_array.append([])     # Yes as an nested array(Makes an Bucket)
        
        largest = max(array)    
        
        # Now we will add element to the buckets according to their Index
        for i in array:
            index = ceil((i * num_of_buckets) / largest)
            # index -1 since index starts from 0
            custom_array[index - 1].append(i)   # first we go target bucket(nested list) then append their
            
        # Now we have all bucket full with elements we need to sort all buckets
        for i in range(num_of_buckets):
            custom_array[i] = bubbleSort(custom_array[i])
        
        # Now that we sorted all the elements in Bucket we need to merge all the buckets
        k = 0   # used to track of index in parameter array
        for i in range(num_of_buckets):       # get the index of each bucket in custom_array
            for j in range(len(custom_array[i])):  # index of all element in each buckets
                # we add the element in parameter array
                array[k] = custom_array[i][j]   # get all elements in Bucket lists(nested lists)
                k += 1
        
        return array

array = [10, 1, 4, 5, 9, 4, 2]
print(bucketSort(array))
