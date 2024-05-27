# Program that will check if the two lists are same they can have same elements 
# at different position 

def is_same(array1 : list, array2 : list) -> None:
    if len(array1) != len(array2):
        print("Not a permutation")
        return
    
    array1 = sorted(array1)
    array2 = sorted(array2)
    
    if array2 == array1:
        print("array1 and array2 is permutation of each other")
    
    else: print("Not a permutation")
    
array1 = ["R","I","S","H","I"]
array2 = ["f","I","I","R","S"]

is_same(array1, array2)