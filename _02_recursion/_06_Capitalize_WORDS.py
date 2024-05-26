# program that will receive a array of words -> return Capitalize array

def capitalize(array : list[str]) -> list[str]:
    last_index : int = len(array) -1
    capitalize_array = [] # empty  now
    
    # just defining not calling it yet
    def recursive_call(array: list, length : int):
        if (length >= 0):
            capitalize_array.append(array[length].upper())
            return recursive_call(array, length -1)
    
    # calling the function to perform recursion
    recursive_call(array, last_index)
    
    capitalize_array.reverse()
    return capitalize_array

myarray : list = ["Hi", "I", "am", "Rishi", "Dubey"]

capitalize_array : list = capitalize(myarray)

print("MY Capitalized array : ",capitalize_array)