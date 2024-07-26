class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int[] mergeSort(int[] nums, int left, int right) {
        if (left >= right) {
            return new int[] { nums[left] };
        }
        int mid = left + (right - left) / 2;
        int[] leftSorted = mergeSort(nums, left, mid);
        int[] rightSorted = mergeSort(nums, mid + 1, right);
        return merge(leftSorted, rightSorted);
    }

    private int[] merge(int[] left, int[] right) {
        int[] sortedArray = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                sortedArray[k++] = left[i++];
            } else {
                sortedArray[k++] = right[j++];
            }
        }
        
        while (i < left.length) {
            sortedArray[k++] = left[i++];
        }
        
        while (j < right.length) {
            sortedArray[k++] = right[j++];
        }
        
        return sortedArray;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] result1 = sol.sortArray(new int[] { 5, 2, 3, 1 });
        System.out.println(Arrays.toString(result1));  // Output: [1, 2, 3, 5]
        
        int[] result2 = sol.sortArray(new int[] { 5, 1, 1, 2, 0, 0 });
        System.out.println(Arrays.toString(result2));  // Output: [0, 0, 1, 1, 2, 5]
    }
}
