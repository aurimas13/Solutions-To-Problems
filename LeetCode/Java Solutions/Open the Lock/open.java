import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));
        if (deadSet.contains("0000")) return -1;
        
        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>("0000", 0));
        Set<String> visited = new HashSet<>();
        visited.add("0000");
        
        while (!queue.isEmpty()) {
            Pair<String, Integer> p = queue.poll();
            String state = p.getKey();
            int depth = p.getValue();
            
            if (state.equals(target)) {
                return depth;
            }
            
            for (int i = 0; i < 4; i++) {
                int digit = state.charAt(i) - '0';
                for (int move : new int[]{-1, 1}) {
                    int nextDigit = (digit + move + 10) % 10;
                    String nextState = state.substring(0, i) + nextDigit + state.substring(i + 1);
                    
                    if (!visited.contains(nextState) && !deadSet.contains(nextState)) {
                        visited.add(nextState);
                        queue.add(new Pair<>(nextState, depth + 1));
                    }
                }
            }
        }
        
        return -1;
    }
}
