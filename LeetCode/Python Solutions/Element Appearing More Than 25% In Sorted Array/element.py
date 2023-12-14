class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4  # 25% of the length of the array

        current_count = 1
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                current_count += 1
                if current_count > threshold:
                    return arr[i]
            else:
                current_count = 1

        return arr[0]  # Handle case for single element array

