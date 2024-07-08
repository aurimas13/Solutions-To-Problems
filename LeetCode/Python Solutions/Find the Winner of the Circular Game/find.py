class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Solving Josephus problem
        winner = 0  # The position of the winner in 0-based index
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1  # Convert to 1-based index
