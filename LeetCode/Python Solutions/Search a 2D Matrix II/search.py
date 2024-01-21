from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        ## O(R+C)
        if not matrix:
            return False
        R = len(matrix)
        C = len(matrix[0])

        r, c = R - 1, 0

        def check_bounds(r, c):
            return (0 <= r < R) and (0 <= c < C)

        while True:
            if check_bounds(r, c):
                if target < matrix[r][c]:
                    ## decrement row
                    r -= 1
                elif target > matrix[r][c]:
                    ## increment col
                    c += 1
                else:
                    ## found the target
                    return True
            else:
                ## out-of-bounds
                return False


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
    # target = 5 -> true | matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
    # target = 20 -> false
    print(Solve)
