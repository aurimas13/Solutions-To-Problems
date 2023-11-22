from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()  # Sorts the cuts list in ascending order
        arr = [0] + cuts + [n]  # Creates a new list 'arr' with 0 at the beginning and 'n' at the end
        dp = [[0] * len(arr) for _ in range(len(arr))]  # Creates a 2D list 'dp' with dimensions 'len(arr) x len(arr)'

        for i in range(len(arr) - 2, -1, -1):
            for j in range(i + 2, len(arr)):
                dp[i][j] = float('inf')  # Initializes 'dp[i][j]' to infinity
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[j] - arr[i])  # Finds the minimum cost by evaluating different combinations

        return dp[0][-1]  # Returns the minimum cost for the entire stick


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 7
    cuts1 = [1, 3, 4, 5]
    result1 = solution.minCost(n1, cuts1)
    print("Minimum cost for test case 1:", result1)  # Expected output: 16

    # Test case 2
    n2 = 9
    cuts2 = [5, 6, 1, 4, 2]
    result2 = solution.minCost(n2, cuts2)
    print("Minimum cost for test case 2:", result2)  # Expected output: 22

    # Test case 3
    n3 = 12
    cuts3 = [2, 3, 7, 9, 10]
    result3 = solution.minCost(n3, cuts3)
    print("Minimum cost for test case 3:", result3)  # Expected output: 35
