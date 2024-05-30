from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        
        # Compute the prefix XOR array
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        
        count = 0
        
        # Find valid (i, j, k) triplets
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)
        
        return count

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countTriplets([2, 3, 1, 6, 7]))  # Output: 4
    print(sol.countTriplets([1, 1, 1, 1, 1]))  # Output: 10
