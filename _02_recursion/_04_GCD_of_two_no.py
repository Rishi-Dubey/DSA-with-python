"""GCD -> Greatest common divisor
ex (12, 8) -> 4 

Euclidean method -> (48, 18)
48/18 -> 2 remainder 12
18/12 -> 1 remainder 6
12/6  -> 2 remainder 0

so GCD -> 6"""

def gcd(num1, num2):
    if num1 > num2:
        remainder = num1 % num2
        if (remainder == 0):
            return num2

        return gcd(num2, remainder)
    
    elif num1 < num2:
        remainder = num2 % num1
        if (remainder == 0):
            return num1

        return gcd(num1, remainder)
    
print("GCD of (48, 18) ->",gcd(48, 18))