from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

        # Too long:

        # counts = {item: nums.count(item) for item in nums}
        # return max(counts, key=lambda k: counts[k])

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.majorityElement([2,2,1,1,1,2,2])  # [2,2,1,1,1,2,2] -> 2
    print(Solve)
