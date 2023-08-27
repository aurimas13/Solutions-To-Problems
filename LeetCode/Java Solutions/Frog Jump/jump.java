import java.util.HashMap;
import java.util.HashSet;

public class Solution {
    public boolean canCross(int[] stones) {
        if (stones == null || stones.length == 0) {
            return false;
        }
        
        int n = stones.length;
        if (n == 1) {
            return true;
        }
        if (stones[1] != 1) {
            return false;
        }
        
        HashMap<Integer, HashSet<Integer>> map = new HashMap<>();
        for (int stone : stones) {
            map.put(stone, new HashSet<>());
        }
        map.get(0).add(0);
        
        for (int stone : stones) {
            for (int step : map.get(stone)) {
                for (int shift = -1; shift <= 1; shift++) {
                    int nextStep = step + shift;
                    if (nextStep <= 0) {
                        continue;
                    }
                    int nextStone = stone + nextStep;
                    if (nextStone == stones[n-1]) {
                        return true;
                    }
                    HashSet<Integer> nextStoneSteps = map.get(nextStone);
                    if (nextStoneSteps != null) {
                        nextStoneSteps.add(nextStep);
                    }
                }
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.canCross(new int[]{0,1,3,5,6,8,12,17}));  // true
        System.out.println(solution.canCross(new int[]{0,1,2,3,4,8,9,11}));  // false
    }
}
