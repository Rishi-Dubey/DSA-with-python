def exponent(num: int, power: int) -> int:
    if power < 0 or int(power) != power:
        raise ValueError("Power should be a non-negative integer")

    elif power == 0:
        return 1
    
    elif power == 1:
        return num
    
    return num * exponent(num, power - 1)

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))

print(f"Result {base}^{power}: {exponent(base, power)}")
