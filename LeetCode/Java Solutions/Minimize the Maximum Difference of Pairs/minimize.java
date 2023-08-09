import java.util.*;

public class Solution {

    public int minimizeMax(int[] nums, int p) {
        if (p == 0) return 0;  // If p is 0, the required difference is 0 as no pairs need to be removed.

        int n = nums.length;
        Arrays.sort(nums);  // Sort the nums array.

        // Construct a set containing differences between consecutive numbers in nums.
        Set<Integer> differences = new HashSet<>();
        for (int i = 1; i < n; i++) {
            differences.add(nums[i] - nums[i - 1]);
        }

        // Convert the set to a list and sort it.
        List<Integer> arr = new ArrayList<>(differences);
        Collections.sort(arr);

        // Use binary search to find the minimum maximum difference.
        int left = 0, right = arr.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (pairCtr(nums, arr.get(mid)) >= p) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // If all values in arr are less than p, return the maximum value in arr.
        // Otherwise, return the value at the found position.
        return left == arr.size() ? arr.get(arr.size() - 1) : arr.get(left);
    }

    private int pairCtr(int[] nums, int mx) {
        int cnt = 0, idx = 1, n = nums.length;
        // Loop through the sorted nums to count pairs having a difference less than or equal to mx.
        while (idx < n) {
            if (nums[idx] - nums[idx - 1] <= mx) {
                cnt++;  // If difference <= mx, increment the count.
                idx++;  // Also, move to the next index.
            }
            idx++;  // Move to the next index.
        }
        return cnt;
    }
}
