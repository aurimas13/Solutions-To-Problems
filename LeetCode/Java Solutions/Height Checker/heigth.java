import java.util.*;

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // Create a frequency map for arr1
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr1) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Create the result list
        List<Integer> result = new ArrayList<>();
        
        // Add elements from arr2 based on their order and frequency
        for (int num : arr2) {
            if (freqMap.containsKey(num)) {
                for (int i = 0; i < freqMap.get(num); i++) {
                    result.add(num);
                }
                freqMap.remove(num);
            }
        }

        // Collect remaining elements
        List<Integer> remaining = new ArrayList<>();
        for (int num : freqMap.keySet()) {
            for (int i = 0; i < freqMap.get(num); i++) {
                remaining.add(num);
            }
        }
        
        // Sort the remaining elements
        Collections.sort(remaining);

        // Add remaining elements to the result
        result.addAll(remaining);

        // Convert result list to array
        int[] resArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            resArray[i] = result.get(i);
        }

        return resArray;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.relativeSortArray(
            new int[]{2,3,1,3,2,4,6,7,9,2,19}, new int[]{2,1,4,3,9,6})));
        System.out.println(Arrays.toString(sol.relativeSortArray(
            new int[]{28,6,22,8,44,17}, new int[]{22,28,8,6})));
    }
}
