from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Create a dictionary to store diagonals
        diagonals = {}

        # Loop through the matrix and populate the diagonals dictionary
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                # If the diagonal does not exist in the dictionary, create it
                if i + j not in diagonals:
                    diagonals[i + j] = []

                # Append the value to the diagonal
                diagonals[i + j].append(val)

        # Traverse the diagonals dictionary and create the result list
        result = [val for k, diagonal in diagonals.items() for val in (reversed(diagonal) if k % 2 == 0 else diagonal)]

        return result


def test_solution():
    s = Solution()

    # Test case 1
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert s.findDiagonalOrder(mat1) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    # Test case 2
    mat2 = [
        [1, 2],
        [3, 4]
    ]
    assert s.findDiagonalOrder(mat2) == [1, 2, 3, 4]

    # Test case 3
    mat3 = [[1]]
    assert s.findDiagonalOrder(mat3) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
