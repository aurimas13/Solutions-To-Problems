class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        # Arrays to store previous and next smaller elements' indices
        prev_smaller = [-1] * n
        next_smaller = [n] * n

        # Find previous smaller element for each element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear the stack for the next pass
        stack.clear()

        # Find next smaller element for each element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        # Calculate the sum of minimums of all subarrays
        ans = sum((i - prev_smaller[i]) * (next_smaller[i] - i) * arr[i] for i in range(n)) % MOD

        return ans
