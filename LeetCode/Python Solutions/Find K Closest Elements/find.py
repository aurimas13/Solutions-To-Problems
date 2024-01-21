from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect
        index = bisect.bisect_left(arr, x)
        left = index - 1
        right = index
        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left + 1:right]
    
# Test Cases:
if __name__ == "__main__":

    assert Solution().findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, -1) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, 6) == [2,3,4,5]
    assert Solution().findClosestElements([1,2,3,4,5], 4, 0) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, 5) == [2,3,4,5]
    
    print("All passed")
