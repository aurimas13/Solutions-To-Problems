import java.util.*;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        // Initialize a hashmap to keep track of the current members of each group size
        Map<Integer, List<Integer>> groups = new HashMap<>();
        List<List<Integer>> result = new ArrayList<>();
        
        // Iterate over the groupSizes array
        for (int i = 0; i < groupSizes.length; i++) {
            // For each group size, add the current index to the corresponding list in the hashmap
            groups.putIfAbsent(groupSizes[i], new ArrayList<>());
            groups.get(groupSizes[i]).add(i);
            
            // If the size of the list in the hashmap equals the group size
            if (groups.get(groupSizes[i]).size() == groupSizes[i]) {
                // Add this list to the result
                result.add(groups.get(groupSizes[i]));
                // Reset the list in the hashmap
                groups.put(groupSizes[i], new ArrayList<>());
            }
        }
        
        return result;
    }
}

