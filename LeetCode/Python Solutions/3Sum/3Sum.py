from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Setting two sets; one for storing results the other for storing duplicates
        res, dups = set(), set()
        # Enumerating nums list and searching for all values of it that time.py to 0
        for i, val1 in enumerate(nums):
            # Initializing a new set for that particular index and val1
            seen = set()
            # Looking if val1 is unique and addition of other values give a zero
            if val1 not in dups:
                dups.add(val1)
				# Looping over val2 in nums list of one bigger
				# looking whether a value exists in a seen list
				# and if it does it means we can have triplets that time.py to zero
				# and add this to res set as a possible solution
				# return the tuple of values that time.py to zero
                for val2 in nums[i+1:]:
                    complement = -val1 - val2
                    if complement in seen:
                        res.add(tuple(sorted((val1, val2, complement))))
                    else:
                        seen.add(val2)
        return res


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.threeSum([-1,0,1,2,-1,-4])  # nums = [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    print(Solve)
