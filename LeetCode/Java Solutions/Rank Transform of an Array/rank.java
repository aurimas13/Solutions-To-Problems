import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // Create a copy of the original array
        int[] sortedArr = Arrays.copyOf(arr, arr.length);
        
        // Sort the copy
        Arrays.sort(sortedArr);
        
        // Create a map to store ranks
        Map<Integer, Integer> rankMap = new HashMap<>();
        
        // Assign ranks to unique elements
        int rank = 1;
        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank++);
            }
        }
        
        // Replace elements with their ranks
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rankMap.get(arr[i]);
        }
        
        return arr;
    }
}