from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)  # Matrix size
        # Comprehend diagonals and sum, avoiding double-counting the center element in odd-sized matrices
        return sum(mat[i][i] + mat[i][n-i-1] for i in range(n)) - (mat[n//2][n//2] if n % 2 else 0)

if __name__ == '__main__':
    s = Solution()
    # Test cases
    test_cases = [
        ([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], 25),
        ([
            [5]
        ], 5),
        ([
            [1, 1],
            [1, 1]
        ], 4)
    ]

    for mat, expected in test_cases:
        result = s.diagonalSum(mat)
        assert result == expected, f"Expected {expected}, but got {result}"
    print("All tests passed!")

