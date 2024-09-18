class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int n = arr.length;
        int[] prefixXor = new int[n + 1];
        
        // Build prefix XOR array
        for (int i = 0; i < n; i++) {
            prefixXor[i + 1] = prefixXor[i] ^ arr[i];
        }
        
        int m = queries.length;
        int[] result = new int[m];
        
        // Process queries
        for (int i = 0; i < m; i++) {
            int left = queries[i][0];
            int right = queries[i][1];
            result[i] = prefixXor[right + 1] ^ prefixXor[left];
        }
        
        return result;
    }
}