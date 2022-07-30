class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1  # left & right
        while l <= r:
            m = l + ((r - l) >> 1)  # mid

            if nums[m] == t: return m

            if nums[l] <= nums[m]:
                # sorted left, see if target lies on left
                if nums[l] <= t < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # sorted right, see if target lies on right
                if nums[m] < t <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
