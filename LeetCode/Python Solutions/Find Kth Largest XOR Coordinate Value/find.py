from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # create an empty list to store all the XOR values
        xor_vals = []
        # loop through each element of the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # calculate the XOR value of the current element using the XOR values of the elements to its top, left, and top-left
                if i > 0:
                    matrix[i][j] ^= matrix[i-1][j]
                if j > 0:
                    matrix[i][j] ^= matrix[i][j-1]
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i-1][j-1]
                # append the XOR value to the list of XOR values
                xor_vals.append(matrix[i][j])
        # sort the list of XOR values in reverse order (highest to lowest) and return the kth element (which is the kth largest XOR value)
        return sorted(xor_vals, reverse=True)[k-1]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 1)
    # matrix = [[5,2],[1,6]], k = 1 -> 7
    # matrix = [[5,2],[1,6]], k = 2 -> 5
    print(Solve)
