class Solution:
    def buildArray(self, target, n):
        operations = []
        current = 0  # Pointer for the current element in the target array

        for num in range(1, n + 1):
            if current >= len(target):
                break  # Stop if we have reached the end of the target array
            operations.append("Push")
            if target[current] == num:
                current += 1  # Move to the next target element
            else:
                operations.append("Pop")  # Pop if the number is not in the target

        return operations
