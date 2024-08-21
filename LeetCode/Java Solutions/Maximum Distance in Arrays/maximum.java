class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int maxDist = 0;
        int minVal = arrays.get(0).get(0);
        int maxVal = arrays.get(0).get(arrays.get(0).size() - 1);
        
        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> array = arrays.get(i);
            int currMin = array.get(0);
            int currMax = array.get(array.size() - 1);
            
            maxDist = Math.max(maxDist, 
                               Math.max(Math.abs(currMax - minVal), 
                                        Math.abs(maxVal - currMin)));
            
            minVal = Math.min(minVal, currMin);
            maxVal = Math.max(maxVal, currMax);
        }
        
        return maxDist;
    }
}