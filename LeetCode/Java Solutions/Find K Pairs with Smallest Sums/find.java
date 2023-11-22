import java.util.*;

class Solution {
    /**
     * Returns the k smallest pairs of integers between two arrays. 
     * The pairs are formed by selecting one element from each of the 
     * input arrays. 
     *
     * @param  nums1  the first input array of integers
     * @param  nums2  the second input array of integers
     * @param  k      the number of smallest pairs to return
     * @return        a list of k pairs of integers sorted in ascending order
     */
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<List<Integer>> heap = new PriorityQueue<>(k, (a, b) -> Integer.compare(b.get(0) + b.get(1), a.get(0) + a.get(1)));

        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (heap.size() < k) {
                    heap.add(Arrays.asList(nums1[i], nums2[j]));
                } else {
                    if (heap.peek().get(0) + heap.peek().get(1) > nums1[i] + nums2[j]) {
                        heap.poll();
                        heap.add(Arrays.asList(nums1[i], nums2[j]));
                    } else {
                        break;
                    }
                }
            }
        }

        List<List<Integer>> res = new ArrayList<>();
        while (!heap.isEmpty()) {
            res.add(0, heap.poll());
        }

        return res;
    }
}

