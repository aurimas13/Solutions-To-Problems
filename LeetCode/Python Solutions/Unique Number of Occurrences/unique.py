class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_map = {}  # Dictionary to count occurrences of each element

        # Count occurrences of each element
        for num in arr:
            if num in occurrence_map:
                occurrence_map[num] += 1
            else:
                occurrence_map[num] = 1

        # Check if all counts are unique
        occurrences = set(occurrence_map.values())
        return len(occurrences) == len(occurrence_map)
