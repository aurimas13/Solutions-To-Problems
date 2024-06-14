class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for seat, student in zip(seats, students):
            moves += abs(seat - student)
        return moves

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    seats = [3, 1, 5]
    students = [2, 7, 4]
    print(sol.minMovesToSeat(seats, students))  # Output: 4
