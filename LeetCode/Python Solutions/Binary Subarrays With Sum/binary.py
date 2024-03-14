class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumCount = collections.defaultdict(int)  # Map to store count of prefix sums
        runningSum = 0
        count = 0
        
        for num in nums:
            # Increment the running sum
            runningSum += num
            # If runningSum equals goal, increment count
            if runningSum == goal:
                count += 1
            # Add to count the number of times (runningSum - goal) has occurred
            count += prefixSumCount[runningSum - goal]
            # Increment the count of runningSum in the map
            prefixSumCount[runningSum] += 1
        
        return count


