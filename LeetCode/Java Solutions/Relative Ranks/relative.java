public class Solution {
    public String[] findRelativeRanks(int[] score) {
        Integer[] indices = new Integer[score.length];
        for (int i = 0; i < score.length; i++) {
            indices[i] = i;
        }
        
        // Sort indices based on the scores in descending order
        Arrays.sort(indices, (a, b) -> Integer.compare(score[b], score[a]));
        
        String[] result = new String[score.length];
        
        // Assign ranks based on sorted order
        for (int rank = 0; rank < indices.length; rank++) {
            if (rank == 0) {
                result[indices[rank]] = "Gold Medal";
            } else if (rank == 1) {
                result[indices[rank]] = "Silver Medal";
            } else if (rank == 2) {
                result[indices[rank]] = "Bronze Medal";
            } else {
                result[indices[rank]] = String.valueOf(rank + 1);
            }
        }
        
        return result;
    }
}
