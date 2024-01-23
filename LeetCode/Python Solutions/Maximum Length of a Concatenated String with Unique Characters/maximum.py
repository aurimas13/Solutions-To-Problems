class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, current_set):
            if index == len(arr):
                return len(current_set)

            max_length = len(current_set)

            # Try to include arr[index] in the set if it has unique characters
            if len(set(arr[index])) == len(arr[index]) and not set(arr[index]).intersection(current_set):
                max_length = max(max_length, backtrack(index + 1, current_set.union(set(arr[index]))))

            # Skip arr[index]
            max_length = max(max_length, backtrack(index + 1, current_set))

            return max_length

        return backtrack(0, set())
