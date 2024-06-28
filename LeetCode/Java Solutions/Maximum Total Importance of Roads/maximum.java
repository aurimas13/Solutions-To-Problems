import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public long maximumImportance(int n, int[][] roads) {
        // Step 1: Count the number of connections for each city
        int[] connections = new int[n];
        for (int[] road : roads) {
            connections[road[0]]++;
            connections[road[1]]++;
        }
        
        // Step 2: Create an array of city indices and sort them based on connections
        Integer[] sortedCities = new Integer[n];
        for (int i = 0; i < n; i++) {
            sortedCities[i] = i;
        }
        Arrays.sort(sortedCities, (a, b) -> connections[b] - connections[a]);
        
        // Step 3: Assign values to cities based on their sorted order
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[sortedCities[i]] = n - i;
        }
        
        // Step 4: Calculate the total importance of all roads
        long totalImportance = 0;
        for (int[] road : roads) {
            totalImportance += values[road[0]] + values[road[1]];
        }
        
        return totalImportance;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maximumImportance(5, new int[][]{{0,1},{1,2},{2,3},{0,2},{1,3},{2,4}}));  // Output: 43
        System.out.println(sol.maximumImportance(5, new int[][]{{0,3},{2,4},{1,3}}));  // Output: 20
    }
}
