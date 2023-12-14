class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Calculates the number of pairs of rows and columns that have the same elements in a given grid.
        :param grid: a list of lists representing the grid to be checked for equal pairs.
        :type grid: List[List[int]]
        :return: the number of pairs of rows and columns that have the same elements.
        :rtype: int
        """
        number_of_pairs = 0
        number_of_rows = len(grid)        
        # Iterate through each row
        for row_index in range(number_of_rows):
            # Create a map with key as column index and value as the element
            row_elements = {col_index: grid[row_index][col_index] for col_index in range(number_of_rows)}
            
            # For each column, check if elements of the current row are equal to elements in the column
            for col_index in range(number_of_rows):
                if self.is_row_equal_to_column(row_elements, grid, col_index):
                    number_of_pairs += 1
                    
        return number_of_pairs

    # Method to check if elements of a row are equal to elements in a column
    def is_row_equal_to_column(self, row_elements, grid, column_index):
        for row_index in range(len(grid)):
            if row_elements[row_index] != grid[row_index][column_index]:
                return False
        return True

# Testing the function with some examples
sol = Solution()
grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(sol.equalPairs(grid1))  # Output should be 1

grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(sol.equalPairs(grid2))  # Output should be 3
