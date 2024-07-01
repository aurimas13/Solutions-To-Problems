import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxDeque = new LinkedList<>();
        Deque<Integer> minDeque = new LinkedList<>();
        int left = 0;
        int result = 0;

        for (int right = 0; right < nums.length; right++) {
            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] <= nums[right]) {
                maxDeque.pollLast();
            }
            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] >= nums[right]) {
                minDeque.pollLast();
            }
            
            maxDeque.addLast(right);
            minDeque.addLast(right);
            
            while (nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()] > limit) {
                left++;
                if (maxDeque.peekFirst() < left) {
                    maxDeque.pollFirst();
                }
                if (minDeque.peekFirst() < left) {
                    minDeque.pollFirst();
                }
            }
            
            result = Math.max(result, right - left + 1);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestSubarray(new int[]{8,2,4,7}, 4));  // Output: 2
        System.out.println(sol.longestSubarray(new int[]{10,1,2,4,7,2}, 5));  // Output: 4
        System.out.println(sol.longestSubarray(new int[]{4,2,2,2,4,4,2,2}, 0));  // Output: 3
    }
}
