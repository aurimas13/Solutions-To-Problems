class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate from the end to the beginning
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                # Return the substring up to and including the odd digit
                return num[:i + 1]
        # If no odd digit is found, return an empty string
        return ""
