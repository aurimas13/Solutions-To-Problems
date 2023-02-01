class Solution:
    @staticmethod
    def convertTime(current: str, correct: str) -> int:
        def to_minutes(time: str) -> int:
            hours, minutes = time.split(':')
            return int(hours) * 60 + int(minutes)

        current_minutes = to_minutes(current)
        correct_minutes = to_minutes(correct)

        minutes_diff = correct_minutes - current_minutes
        if minutes_diff < 0:
            minutes_diff += 1440

        steps = [60, 15, 5, 1]
        count = 0
        for step in steps:
            while minutes_diff >= step:
                count += 1
                minutes_diff -= step

        return count

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minKnightMoves(current = "02:30", correct = "04:35")
    # current = "02:30", correct = "04:35" -> 3
    # current = "11:00", correct = "11:01" -> 1
    print(Solve)
