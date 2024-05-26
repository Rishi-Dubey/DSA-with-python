# program will find the missing number in array of 1 - 100 numbers

"""Since numbers are natural we can use formula
Sum of (n) natural numbers = n(n + 1) / 2

so n(n + 1)/ 2 = sum(array) + missing no."""

array = [i for i in range(1, 101)]
array.remove(20)


def find_missing_number(array : list) -> int:
    sum_of_array = sum(array)
    n = len(array) + 1  #  len of sequence after a missing no
    expected_sum = n * (n + 1) / 2
    
    missing_no = expected_sum - sum_of_array
    return int(missing_no)
    
missing_no : int = find_missing_number(array)

print("Missing number :", missing_no)