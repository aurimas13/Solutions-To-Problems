import java.util.*;

class Solution {
    private static final int X_INDEX = 0;
    private static final int Y_INDEX = 1;
    private static final int R_INDEX = 2;
    private static final int ID_INDEX = 3;

    public int maximumDetonation(int[][] bombs) {
        Map<Integer, List<int[]>> bombGraph = createBombGraph(bombs);
        return findLargestDetonation(bombGraph);
    }

    private int findLargestDetonation(Map<Integer, List<int[]>> bombGraph) {
        int maxDetonation = 0;
        Set<Integer> visitedBombs = new HashSet<>();

        for (Integer bombId : bombGraph.keySet()) {
            if (visitedBombs.contains(bombId)) continue;
            maxDetonation = Math.max(maxDetonation, detonateBomb(bombGraph, new HashSet<>(), visitedBombs, bombId));
        }

        return maxDetonation;
    }

    private int detonateBomb(Map<Integer, List<int[]>> bombGraph, Set<Integer> visited, Set<Integer> allVisited, Integer bombId) {
        if (visited.contains(bombId)) return 0;

        allVisited.add(bombId);
        visited.add(bombId);

        int detonationCount = 1;
        for (int[] neighbourBomb : bombGraph.get(bombId)) {
            int neighbourBombId = neighbourBomb[ID_INDEX];
            detonationCount += detonateBomb(bombGraph, visited, allVisited, neighbourBombId);
        }

        return detonationCount;
    }

    private Map<Integer, List<int[]>> createBombGraph(int[][] bombs) {
        Map<Integer, List<int[]>> bombGraph = new HashMap<>();

        for (int bombId = 0; bombId < bombs.length; bombId++) {
            int[] bomb = bombs[bombId];
            bombGraph.putIfAbsent(bombId, new ArrayList<>());

            for (int neighbourBombId = 0; neighbourBombId < bombs.length; neighbourBombId++) {
                if (bombId == neighbourBombId) continue; // same bomb

                if (isWithinRange(bomb, bombs[neighbourBombId])) {
                    bombGraph.get(bombId).add(createBombEntry(bombs[neighbourBombId], neighbourBombId));
                }
            }
        }

        return bombGraph;
    }

    // Creating bomb array with ID for readability.
    private int[] createBombEntry(int[] bomb, int id) {
        return new int[]{bomb[X_INDEX], bomb[Y_INDEX], bomb[R_INDEX], id};
    }

    // Returns true if the second bomb is within the range of the first bomb
    private boolean isWithinRange(int[] bomb1, int[] bomb2) {
        double distance = Math.sqrt(Math.pow(bomb2[X_INDEX] - bomb1[X_INDEX], 2) + Math.pow(bomb2[Y_INDEX] - bomb1[Y_INDEX], 2));
        return distance <= bomb1[R_INDEX];
    }
}

