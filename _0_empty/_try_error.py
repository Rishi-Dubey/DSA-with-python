class Solution:
    def twoSum(self, array: list[int], target: int) -> list[int]:
        flag = 0
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == target:
                    return [i, j]
    
array = [1, 2, 3, 4, 5]
target = 5

sol =  Solution()
print(sol.twoSum(array, target))