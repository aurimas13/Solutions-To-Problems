class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        li = list(map(str, s.split()))
        for i in li:
            if i.isdigit():
                nums.append(i)
        nums = list(map(int, nums))
        for n in range(len(nums) - 1):
            if nums[n] >= nums[n + 1]:
                return False
        return True
        
        # if sorted(nums) == nums:
        #     return True
        # else:
        #     return False

# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.areNumbersAscending("hello world 5 x 5")  # "1 box has 3 blue 4 red 6 green and 12 yellow marbles" - true | "hello world 5 x 5" - false
    print(Solve)
