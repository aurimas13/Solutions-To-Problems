import java.util.*;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        int m = mat.length;
        int[] result = new int[k];
        
        // Pair<int[], Integer> for (count, index)
        List<Pair> counts = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            int count = 0;
            for (int j = 0; j < mat[i].length; j++) {
                count += mat[i][j];
            }
            counts.add(new Pair(count, i));
        }
        
        Collections.sort(counts);
        
        for (int i = 0; i < k; i++) {
            result[i] = counts.get(i).index;
        }
        
        return result;
    }
    
    class Pair implements Comparable<Pair> {
        int count;
        int index;

        Pair(int count, int index) {
            this.count = count;
            this.index = index;
        }

        @Override
        public int compareTo(Pair o) {
            if (this.count == o.count) {
                return Integer.compare(this.index, o.index);
            }
            return Integer.compare(this.count, o.count);
        }
    }
}
