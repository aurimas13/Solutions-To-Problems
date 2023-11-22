from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[matrix[-j-1][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return (matrix[:]) # Delete this when running in LeetCode


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])  #  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] ->  [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(Solve)
