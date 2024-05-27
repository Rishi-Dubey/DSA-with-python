"""Program will find the target in the given array"""

class Solutions:
    def search(self, array : list, target) -> None:
        for i in range(len(array)):
            if array[i] == target:
                print(f"Found -> array[{i}] = {target}")
                break
        else:
            print(f"{target} not found")
          
array = [1, 2, 3, 4, 5, 23, 34, 342]  
sol = Solutions()
sol.search(array, 23)