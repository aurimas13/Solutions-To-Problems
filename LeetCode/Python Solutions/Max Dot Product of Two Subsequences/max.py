class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # Initialize the dp table with negative infinity values
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        # Iterate through both arrays
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Current dot product
                curr = nums1[i-1] * nums2[j-1]
                
                # Update dp value based on the four options discussed above
                dp[i][j] = max(curr, dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + curr)
        
        # Return the result from the bottom-right corner of the dp table
        return dp[n][m]
