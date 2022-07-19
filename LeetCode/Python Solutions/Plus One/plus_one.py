from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer_from_array = int("".join(str(e) for e in digits))
        incremented_integer = integer_from_array + 1
        new_array = [int(i) for i in str(incremented_integer)]
        return new_array


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.plusOne(digits = [1,2,3]) # digits = [1,2,3] ->[1,2,4] | digits = [4,3,2,1] -> [4,3,2,2]
    print(Solve)
