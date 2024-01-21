from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result, modulo = 0, 10**9 + 7

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                result += pow(2, right - left, modulo)
                left += 1

        return result % modulo

def test_solution():
    s = Solution()
    assert s.numSubseq([3,5,6,7], 9) == 4
    assert s.numSubseq([3,3,6,8], 10) == 6
    assert s.numSubseq([2,3,3,4,6,7], 12) == 61
    assert s.numSubseq([1,1,2,2,3,3,4,4,5,5], 8) == 1011
    assert s.numSubseq([1,2,3,4,5,6,7,8,9,10], 10) == 341
    print("All tests passed!")

    
if __name__ == '__main__':
    test_solution()