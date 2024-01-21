class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Use diagonal argument to find a unique string
        unique_str = ''
        for i, str in enumerate(nums):
            # Flip the ith bit of the ith string
            unique_str += '1' if str[i] == '0' else '0'
        return unique_str
