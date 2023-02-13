class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # reverse the digits of each integer and store it in a set
        reversed_nums = {int(str(num)[::-1]) for num in nums} | set(nums)
        return len(reversed_nums)

# Checking in Terminal/Console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countDistinctIntegers(nums = [1,13,10,12,31])
    # nums = [1,13,10,12,31] -> 6
    # nums = [2,2,2] -> 1
    print(Solve)



    
