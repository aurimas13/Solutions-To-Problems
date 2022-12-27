from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #number of elements in a row starting from zero
        n = len(matrix[0])-1
        #for loop for row at a time
        for rows in matrix:
            #check condition if target is in between first and last element
            if(rows[0]<= target and rows[n]>=target):
                #if yes then search target for each val of rows
                for val in rows:
                    #if found return true
                    if(val==target):
                        return True
        return False


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 )
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 -> true
    print(Solve)
