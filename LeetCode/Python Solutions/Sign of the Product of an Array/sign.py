from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1

        for num in nums:
            product *= num

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        

# Tests:
if __name__ == '__main__':
    sol = Solution()  # create an instance of Solution
    assert sol.arraySign([-1,-2,-3,-4,3,2,1]) == 1, "Should be 1"
    assert sol.arraySign([1,5,0,2,-3]) == 0, "Should be 0"
    assert sol.arraySign([-1,1,-1,1,-1]) == -1, "Should be -1"
    assert sol.arraySign([1,2,3]) == 1, "Should be 1"
    assert sol.arraySign([-1,-2,-3]) == -1, "Should be -1"
    assert sol.arraySign([0,-1,-2,-3,-4]) == 0, "Should be 0"

    print("All passed")
