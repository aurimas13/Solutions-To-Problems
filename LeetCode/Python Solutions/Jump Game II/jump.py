from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        max_reachable = max_steps = nums[0]
        jumps = 1
        
        for i in range(1, n):
            if i > max_steps:
                max_steps = max_reachable
                jumps += 1
            
            max_reachable = max(max_reachable, i + nums[i])
        
        return jumps

# Tests:
if __name__ == '__main__':
    def test_solution():
        s = Solution()
        
        assert s.jump([2, 3, 1, 1, 4]) == 2
        assert s.jump([1, 1, 1, 1, 1, 1]) == 5
        assert s.jump([5, 4, 3, 2, 1, 1, 1]) == 1
        assert s.jump([2, 3, 0, 1, 4]) == 2
        assert s.jump([1, 2, 3, 4, 5, 6, 7, 8]) == 4
        assert s.jump([2, 2, 2, 2, 2, 2]) == 3
        assert s.jump([]) == 0
        assert s.jump([1]) == 0

    test_solution()
    print('All tests passed')
