import java.util.*;


class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int diff = arr[1] - arr[0];

        for(int i = 2; i < arr.length; i++) {
            if(arr[i] - arr[i - 1] != diff) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.canMakeArithmeticProgression(new int[]{3, 5, 1})); // Should print: true
        System.out.println(s.canMakeArithmeticProgression(new int[]{1, 2, 4})); // Should print: false
    }
}
