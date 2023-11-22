from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while top <= bottom and left <= right:
            # Traverse right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse down
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse up
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                
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
