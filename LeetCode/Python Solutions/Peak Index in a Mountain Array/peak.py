from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left


# Checking in Terminal/Console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.peakIndexInMountainArray(arr = [0,2,1,0])  
    # arr = [0,1,0] -> 1
    # arr = [0,2,1,0] -> 1
    print(Solve)
