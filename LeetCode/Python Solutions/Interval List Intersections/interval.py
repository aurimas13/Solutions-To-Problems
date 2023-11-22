from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        combined = []
        i, j = 0, 0

        # Iterate through both lists of intervals
        while i < len(firstList) and j < len(secondList):
            # Calculate the intersection of the current intervals
            low_ints = max(firstList[i][0], secondList[j][0])
            high_ints = min(firstList[i][1], secondList[j][1])

            # If the intersection exists, append it to the combined list
            if low_ints <= high_ints:
                combined.append([low_ints, high_ints])

            # Move to the next interval in the list with the smaller endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return combined

if __name__ == '__main__':
    s = Solution()

    # Test cases
    test_cases = [
        ({"firstList": [[0, 2], [5, 10], [13, 23], [24, 25]], "secondList": [[1, 5], [8, 12], [15, 24], [25, 26]]},
         [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.intervalIntersection(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
