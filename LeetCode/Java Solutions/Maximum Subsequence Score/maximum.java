import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        // Create a HashMap to store the mapping of each element in nums2 to a list of corresponding elements from nums1
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        // Populate the HashMap
        for (int i = 0; i < nums1.length; i++) {
            if (!map.containsKey(nums2[i])) {
                ArrayList<Integer> list = new ArrayList<>();
                list.add(nums1[i]);
                map.put(nums2[i], list);
            } else {
                ArrayList<Integer> list = map.get(nums2[i]);
                list.add(nums1[i]);
                map.put(nums2[i], list);
            }
        }

        // Sort nums2 in ascending order
        Arrays.sort(nums2);

        // Update nums1 by choosing elements from the HashMap based on the sorted order of nums2
        for (int i = 0; i < nums2.length; i++) {
            ArrayList<Integer> list = map.get(nums2[i]);
            nums1[i] = list.get(0);
            list.remove(0);
            if (list.size() > 0) {
                map.put(nums2[i], list);
            } else {
                map.remove(nums2[i]);
            }
        }

        long sum = 0;
        ArrayList<Integer> list = new ArrayList<>();

        // Calculate the sum of the last k elements in nums1 and maintain a sorted list of these elements
        for (int i = nums1.length - 1; i >= nums1.length - k; i--) {
            sum += nums1[i];
            if (list.size() == 0) {
                list.add(nums1[i]);
            } else {
                int index = 0;
                int low = 0, high = list.size() - 1;
                while (low <= high) {
                    int mid = (low + high) / 2;
                    if (list.get(mid) >= nums1[i]) {
                        index = mid;
                        high = mid - 1;
                    } else {
                        index = mid + 1;
                        low = mid + 1;
                    }
                }
                list.add(index, nums1[i]);
            }
        }

        long result = nums2[nums1.length - k] * sum;

        // Calculate the maximum result by considering elements before the last k elements in nums1
        for (int i = nums1.length - k - 1; i >= 0; i--) {
            int index = 0;
            int low = 0, high = list.size() - 1;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (list.get(mid) >= nums1[i]) {
                    index = mid;
                    high = mid - 1;
                } else {
                    index = mid + 1;
                    low = mid + 1;
                }
            }
            if (index != 0) {
                list.add(index, nums1[i]);
                sum = sum - list.get(0);
                sum = sum + nums1[i];
                list.remove(0);
                long ans = sum * nums2[i];
                if (ans > result) {
                    result = ans;
                }
            }
        }

        return result;
    }
}
