from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix and matrix[-1]:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result

# Tests:
if __name__ == '__main__':
    s = Solution()
    # test case 1
    output1 = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    expected_output1 = [1,2,3,6,9,8,7,4,5]
    assert output1 == expected_output1, f"Expected {expected_output1}, but got {output1}"
    # test case 2
    output2 = s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    expected_output2 = [1,2,3,4,8,12,11,10,9,5,6,7]
    assert output2 == expected_output2, f"Expected {expected_output2}, but got {output2}"
    # test case 3
    output3 = s.spiralOrder([])
    expected_output3 = []
    assert output3 == expected_output3, f"Expected {expected_output3}, but got {output3}"
    print("All tests passed!")
    