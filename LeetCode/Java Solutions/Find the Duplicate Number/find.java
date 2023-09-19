public class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Detecting the loop using Floyd's Cycle Detection
        int tortoise = nums[0];
        int hare = nums[0];

        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);

        // Phase 2: Finding the starting point of the cycle
        hare = nums[0];
        while (hare != tortoise) {
            hare = nums[hare];
            tortoise = nums[tortoise];
        }

        return hare;
    }
}

