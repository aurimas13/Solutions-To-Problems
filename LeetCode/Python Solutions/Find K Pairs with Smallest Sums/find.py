import java.util.*;

class Solution {
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
