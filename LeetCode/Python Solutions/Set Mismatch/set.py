class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Length of the input array
        num_set = set()  # Set to keep track of seen numbers
        duplicated = -1  # Variable to store the duplicated number

        # Iterate over the array to find the duplicated number
        for num in nums:
            if num in num_set:
                duplicated = num  # Found the duplicated number
            num_set.add(num)  # Add the current number to the set

        # Iterate from 1 to n to find the missing number
        for i in range(1, n + 1):
            if i not in num_set:
                return [duplicated, i]  # Return the duplicated and missing number
