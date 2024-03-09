class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        // Initialize two pointers for both arrays
        int i = 0, j = 0;
        
        while (i < nums1.length && j < nums2.length) {
            // If a common element is found, return it
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            }
            // Move the pointer of the smaller element
            else if (nums1[i] < nums2[j]) {
                i++;
            }
            else {
                j++;
            }
        }
        
        // If no common element is found
        return -1;
    }
}
