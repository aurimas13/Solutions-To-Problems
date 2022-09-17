from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            # Each triangle element is equal to the skyline.py of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
                print(row)
            triangle.append(row)

        return triangle

# OR
#         if numRows   == 0: return []
#         elif numRows == 1: return [[1]]
#         Tri = [[1]]
#         for i in range(1,numRows):
#             row = [1]
#             for j in range(1,i):
#                 row.append(Tri[i-1][j-1] + Tri[i-1][j])
#             row.append(1)
#             Tri.append(row)
#         return Tri


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.generate(numRows = 5)  #  5 -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(Solve)