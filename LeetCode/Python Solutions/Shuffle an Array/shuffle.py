from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        import random
        nums = self.nums.copy()
        random.shuffle(nums)
        return nums

    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Test Cases:
if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print(param_1)
    print(param_2)
    print(obj.nums)
    print(nums)
    assert param_1 == nums
    assert param_2 != nums
    print("All passed")
