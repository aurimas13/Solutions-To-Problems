class Solution:
    def totalMoney(self, n: int) -> int:
        # Number of complete weeks
        weeks = n // 7
        # Number of days in the incomplete week
        remainingDays = n % 7

        # Total savings in complete weeks
        total = (7 * (1 + 7) // 2) * weeks  # Sum of 1..7 multiplied by number of weeks
        # Additional savings each week
        total += 7 * (weeks * (weeks - 1) // 2)

        # Savings in the remaining days of the last week
        startDay = weeks + 1  # Starting amount for the last incomplete week
        total += sum(startDay + i for i in range(remainingDays))

        return total

