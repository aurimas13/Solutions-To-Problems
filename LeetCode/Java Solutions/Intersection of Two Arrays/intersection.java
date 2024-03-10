class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Use HashSet for removing duplicates and for efficient lookups
        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }
        
        Set<Integer> intersection = new HashSet<>();
        for (int num : nums2) {
            if (set1.contains(num)) {
                intersection.add(num);
            }
        }
        
        // Convert the intersection set to an array
        int[] result = new int[intersection.size()];
        int i = 0;
        for (Integer num : intersection) {
            result[i++] = num;
        }
        
        return result;
    }
}
