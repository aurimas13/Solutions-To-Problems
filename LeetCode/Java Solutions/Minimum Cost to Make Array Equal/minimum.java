import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

// Define a new class WeightedNum which will be used to store each number with its associated weight
class WeightedNum implements Comparable<WeightedNum> {
    public int num;
    public int weight;

    // Constructor for the WeightedNum class
    public WeightedNum(int num, int weight) {
        this.num = num;
        this.weight = weight;
    }

    // Override the compareTo method to sort by the num field
    @Override
    public int compareTo(WeightedNum other) {
        return num - other.num;
    }
}

class Solution {
    public long minCost(int[] nums, int[] cost) {
        // Create a list of WeightedNums, each consisting of a number and its associated weight
        // This list is sorted by the number
        List<WeightedNum> weightedNums = IntStream
                .range(0, nums.length)
                .boxed()
                .map(i -> new WeightedNum(nums[i], cost[i]))
                .sorted()
                .toList();

        // Calculate the total weight by summing all the weights
        long totalWeight = 0;
        for (int weight : cost) totalWeight += weight;

        // Initialize current running weight and the number to minimize to
        long currentRunningWeight = 0L;
        int numberToMinimizeTo = 0;

        // Iterate through the sorted list of weighted numbers
        // If the current running weight exceeds half of the total weight, set the current number as the number to minimize to
        for (WeightedNum weightedNum : weightedNums) {
            currentRunningWeight += weightedNum.weight;
            if ((double) currentRunningWeight / (double) totalWeight >= 0.5) {
                numberToMinimizeTo = weightedNum.num;
                break;
            }
        }

        // Store the number to minimize to
        final int number = numberToMinimizeTo;

        // Return the minimum cost by summing the product of the absolute difference between each number and the number to minimize to and its weight
        // Only consider numbers that are not equal to the number to minimize to
        return weightedNums
                .stream()
                .filter(x -> x.num != number)
                .reduce(0L, (acc, weightedNum) -> acc + (long)Math.abs(weightedNum.num - number) * weightedNum.weight, Long::sum);
    }
}

