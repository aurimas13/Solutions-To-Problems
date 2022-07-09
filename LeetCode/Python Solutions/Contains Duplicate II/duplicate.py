from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # maintain the last seen index of an element
        last_occurence = {}
        for i, x in enumerate(nums):
            # check if last seen index of current element is within window k
            if x in last_occurence and i - last_occurence[x] <= k:
                return True
            last_occurence[x] = i
        return False


# Check in the console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.containsNearbyDuplicate([1,2,3,1], 3)  # nums = [1,2,3,1], k = 3 -> true | nums = [1,2,3,1,2,3], k = 2 -> false
    print(Solve)