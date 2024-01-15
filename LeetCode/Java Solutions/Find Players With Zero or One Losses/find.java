import java.util.*;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        // Sets for players with no losses and exactly one loss
        Set<Integer> noLosses = new HashSet<>();
        Set<Integer> oneLoss = new HashSet<>();

        // Map to keep track of the number of losses for each player
        Map<Integer, Integer> lossCount = new HashMap<>();

        for (int[] match : matches) {
            int winner = match[0];
            int loser = match[1];

            // Add winner to noLosses set
            noLosses.add(winner);

            // Update loss count for the loser
            if (lossCount.containsKey(loser)) {
                lossCount.put(loser, lossCount.get(loser) + 1);
                // If a player's loss count reaches 2, remove them from oneLoss
                if (lossCount.get(loser) == 2) {
                    oneLoss.remove(loser);
                }
            } else {
                // For first loss, add to oneLoss and set loss count to 1
                lossCount.put(loser, 1);
                oneLoss.add(loser);
            }
        }

        // Remove players from noLosses who have lost any match
        for (int player : lossCount.keySet()) {
            noLosses.remove(player);
        }

        // Convert sets to sorted lists
        List<Integer> noLossesList = new ArrayList<>(noLosses);
        List<Integer> oneLossList = new ArrayList<>(oneLoss);
        Collections.sort(noLossesList);
        Collections.sort(oneLossList);

        // Return lists of players with no losses and exactly one loss
        List<List<Integer>> result = new ArrayList<>();
        result.add(noLossesList);
        result.add(oneLossList);

        return result;
    }
}