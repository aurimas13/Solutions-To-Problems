class Solution:
    # Function to find the first non-repeating character in
    # the string by doing only a single traversal of it
    @staticmethod
    def firstUniqChar(s: str) -> int:
        # base case
        if not s:
            return -1

        # dictionary to store character count and the index of its
        # last occurrence in the string
        d = {}

        for index, char in enumerate(s):
            frequency, prevIndex = d.get(char, (0, index))
            d[char] = (frequency + 1, index)

        # stores index of the first non-repeating character
        min_index = -1

        # Traverse the dictionary and find a character with count 1 and
        # a minimum index of the string
        for key, values in d.items():
            count, firstIndex = values
            if count == 1 and (min_index == -1 or firstIndex < min_index):
                min_index = firstIndex

        return min_index


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.firstUniqChar(s = "loveleetcode")
    # s = "loveleetcode" -> 2
    # s = "leetcode" -> 0
    print(Solve)
