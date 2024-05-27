"""Program that will rotate a 2D matrix by 90 degree"""

import numpy as np

class Solution:
    def rotate_by_90(self, array_2D) -> None:
        
        copy_array = np.zeros_like(array_2D)

        # we know after rotating row(0) -> row[0][0],row[0][1],row[0][2] -> col[0,3],col[1][3],col[2][3]
        for row in range(len(array_2D)):
            for col in range(len(array_2D[0])):
                copy_array[col][len(array_2D)-1-row] = array_2D[row][col] 
        
        return copy_array
    
array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2D)
print()

sol = Solution()
array_2D = sol.rotate_by_90(array_2D)

print(array_2D)