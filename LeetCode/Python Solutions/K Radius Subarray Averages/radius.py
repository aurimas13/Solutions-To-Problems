class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)  # Get the length of nums list
        result = [-1] * n  # Initialize the result list with size n and all elements as -1
        prefixSum = [0] * (n + 1)  # Initialize the prefix sum list with size n + 1 and all elements as 0

        # Generate the prefix sum list
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]  # Update the prefix sum list by adding the current number

        # Calculate the k-radius average for each index
        for i in range(n):
            if i - k >= 0 and i + k < n:  # Check if it's possible to create a subarray centered at i with radius k
                sum = prefixSum[i + k + 1] - prefixSum[i - k]  # Calculate the sum of the subarray
                result[i] = sum // (2 * k + 1)  # Calculate the average and store it in the result list
        return result  # Return the result list

