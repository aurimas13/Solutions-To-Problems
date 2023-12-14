from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix
    
# Tests:
if __name__ == '__main__':
    s = Solution()
    # test case 1
    output1 = s.generateMatrix(3)
    expected_output1 = [[1,2,3],[8,9,4],[7,6,5]]
    assert output1 == expected_output1, f"Expected {expected_output1}, but got {output1}"
    # test case 2
    output2 = s.generateMatrix(1)
    expected_output2 = [[1]]
    assert output2 == expected_output2, f"Expected {expected_output2}, but got {output2}"
    print("All tests passed!")

# # My 2nd solution
# 
# class Solution:
#     @staticmethod
#     def generateMatrix(n: int) -> List[List[int]]:
#         matrix = [[None for i in range(n)] for i in range(n)]
#         values = [i for i in range(n ** 2, 0, -1)]
#         turn_left = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
#         c = (n // 2, n // 2 - 1) if n % 2 == 0 else (n // 2, n // 2)

#         x, y = c
#         orient = (1, 0) if n % 2 == 0 else (-1, 0)
#         for i in range(n ** 2):
#             val = values[i]
#             matrix[x][y] = val

#             turn_dx, turn_dy = turn_left.get(orient)

#             if x + turn_dx in range(0, n) and y + turn_dy in range(0, n) and matrix[x + turn_dx][y + turn_dy] is None:
#                 orient = (turn_dx, turn_dy)

#             x, y = x + orient[0], y + orient[1]  # continue path
#         return matrix


# # Checking in console
# if __name__ == '__main__':
#     Instant = Solution()
#     Solve = Instant.generateMatrix(n=3)
#     # n=3 -> [[1,2,3],[8,9,4],[7,6,5]] | n=1 -> [[1]]
#     print(Solve)
