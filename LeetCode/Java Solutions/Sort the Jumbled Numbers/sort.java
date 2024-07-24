import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        // Create a new array of the same length to hold the mapped values and indices
        int[][] mappedValues = new int[nums.length][2];

        for (int i = 0; i < nums.length; i++) {
            int mappedValue = mapValue(mapping, nums[i]);
            mappedValues[i][0] = mappedValue;
            mappedValues[i][1] = i;
        }

        // Sort the array based on the mapped values and then indices for stability
        Arrays.sort(mappedValues, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] != b[0]) {
                    return Integer.compare(a[0], b[0]);
                } else {
                    return Integer.compare(a[1], b[1]);
                }
            }
        });

        // Create the result array based on the sorted order
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = nums[mappedValues[i][1]];
        }

        return result;
    }

    private int mapValue(int[] mapping, int num) {
        StringBuilder mappedStr = new StringBuilder();
        for (char digit : String.valueOf(num).toCharArray()) {
            mappedStr.append(mapping[digit - '0']);
        }
        return Integer.parseInt(mappedStr.toString());
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.sortJumbled(new int[]{8,9,4,0,2,1,3,5,7,6}, new int[]{991,338,38})));  // Output: [338,38,991]
        System.out.println(Arrays.toString(sol.sortJumbled(new int[]{0,1,2,3,4,5,6,7,8,9}, new int[]{789,456,123})));  // Output: [123,456,789]
    }
}
