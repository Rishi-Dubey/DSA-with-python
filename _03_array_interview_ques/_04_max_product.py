"""Program will find the maximum product in array which consists of only positive int"""

class Solutions:
    def max_product(array : list[int]) -> None:
        if len(array) < 2:
            print("Array does not have enough elements to find a product.")
            return None
        
        max_1 = 0 # assume
        max_2 = 1 # assume
        
        for i in range(len(array)):
            if array[i] > array[max_1]:
                max_2 = max_1
                max_1 = i
                
            elif array[i] > array[max_2] and array[max_2] < array[max_1]:
                max_2 = i
            
        print(max_1, max_2)
        print(f"Max Product : array[{max_1}] * array[{max_2}] = {array[max_2]*array[max_1]} ")
    
Solutions.max_product([1, 2, 3, 10, 4, 5, 9])