class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""

        for i in range(len(num) - 2):
            # Check if the substring of length 3 has the same character
            if num[i] == num[i + 1] == num[i + 2]:
                # Update max_good if the current substring is greater
                max_good = max(max_good, num[i:i + 3])

        return max_good
