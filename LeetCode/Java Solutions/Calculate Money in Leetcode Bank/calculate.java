public class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int remainingDays = n % 7;

        // Total savings in complete weeks
        int total = (7 * (1 + 7) / 2) * weeks;  // Sum of 1..7 multiplied by number of weeks
        // Additional savings each week
        total += 7 * (weeks * (weeks - 1) / 2);

        // Savings in the remaining days of the last week
        int startDay = weeks + 1;
        for (int i = 0; i < remainingDays; i++) {
            total += startDay + i;
        }

        return total;
    }
}
