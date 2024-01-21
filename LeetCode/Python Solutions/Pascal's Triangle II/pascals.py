from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        Triangle = [[1]]
        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(Triangle[i - 1][j - 1] + Triangle[i - 1][j])
            row.append(1)
            Triangle.append(row)
        return row


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.getRow(3)  # 3 -> [1,3,3,1]
    print(Solve)

