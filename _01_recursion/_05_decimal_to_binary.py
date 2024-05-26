# To convert decimal to binary
# 12 -> divided by 2 : remainder(0)
# 6 ->  divided by 2 : remainder(0)
# 3 ->  divided by 2 : remainder(1)
# 1 -> return 1 

# decimal(12) -> 1100

def decimal_to_binary(num : int):
    quotient : int = num // 2
    remainder : int = num % 2
    if (num < 0 or int(num) != num):
        raise ValueError("Only positive integer and zero allowed!!!")
    
    elif (num in [0,1]):
        return str(num)
    
    return decimal_to_binary(quotient) + str(remainder)
    
    
print(f"Decimal(11) -> binary({decimal_to_binary(0)})")
    
    