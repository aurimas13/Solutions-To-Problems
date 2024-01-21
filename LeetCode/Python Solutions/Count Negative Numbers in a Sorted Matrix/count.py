class Solution:
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Corner case: if the grid is null or empty, return 0
        if not grid or not grid[0]:
            return 0
        
        # Get the dimensions of the matrix
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Start from the top-right corner of the matrix
        row = 0
        col = colCount - 1
        
        # Counter for negative numbers
        negativeCount = 0
        
        # Traverse the matrix
        while row < rowCount and col >= 0:
            # If the current element is negative
            if grid[row][col] < 0:
                # All elements below this element in the current column are negative
                # (as columns are sorted in non-increasing order).
                # So, add the number of elements below it to the negative count.
                negativeCount += rowCount - row
                
                # Move to the left in the same row
                col -= 1
            else:
                # If the current element is non-negative,
                # move down to the next row.
                row += 1
                
        return negativeCount


# Example usage
solution = Solution()
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]
print(solution.countNegatives(grid))  # Output: 8
