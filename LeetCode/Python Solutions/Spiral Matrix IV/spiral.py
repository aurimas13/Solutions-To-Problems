class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        top, bottom, left, right = 0, m - 1, 0, n - 1
        current = head
        
        while current and top <= bottom and left <= right:
            # Traverse top row
            for col in range(left, right + 1):
                if current:
                    matrix[top][col] = current.val
                    current = current.next
                else:
                    return matrix
            top += 1
            
            # Traverse right column
            for row in range(top, bottom + 1):
                if current:
                    matrix[row][right] = current.val
                    current = current.next
                else:
                    return matrix
            right -= 1
            
            if top <= bottom:
                # Traverse bottom row
                for col in range(right, left - 1, -1):
                    if current:
                        matrix[bottom][col] = current.val
                        current = current.next
                    else:
                        return matrix
                bottom -= 1
            
            if left <= right:
                # Traverse left column
                for row in range(bottom, top - 1, -1):
                    if current:
                        matrix[row][left] = current.val
                        current = current.next
                    else:
                        return matrix
                left += 1
        
        return matrix