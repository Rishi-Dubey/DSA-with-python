"""Program will find the pair(index) whose sum is equal to target
ex -> array = [1, 2, 3, 4, 5] , target -> 5
So pair(2,3) means array[1] + array[2] -> have sum(5)"""

def pair_sum(array : list[int], target : int) -> None:
    flag = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                print(f"Output : ({array[i], array[j]})")
                print(f"Array[{i}] + Array[{j}] = {target}")
                flag = 1
                break
        if flag == 1:
            break

array = [1, 2, 3, 4, 5]
target = 5

pair_sum(array, target)