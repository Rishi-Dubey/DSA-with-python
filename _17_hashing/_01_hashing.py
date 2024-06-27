"""Hashing have 3 things first 
Input -> hash function -> Output

Hashing convert our data in to some hash function output which can be use to store in Array
or access array's that particular index
It can also be used as Security measure since hash function convert data in to some other value

Python hash function is Dict{}"""


def modNumber(num : int, arrayLen : int):
    remainder = num % arrayLen
    return remainder

def modString(word : str, arrayLen : int):
    sum = 0     # store the sum of ASCII value of String
    for i in word:
        sum += ord(i)   # Return the ASCII value of character
    remainder = sum % arrayLen
    return remainder

print(modString("Rishi", 10))
print(ord("A"))