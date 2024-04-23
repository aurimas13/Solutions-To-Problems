import java.util.*;

public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n <= 2) {
            List<Integer> roots = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                roots.add(i);
            }
            return roots;
        }

        // Initialize the graph
        List<Set<Integer>> neighbors = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            neighbors.add(new HashSet<>());
        }
        for (int[] edge : edges) {
            neighbors.get(edge[0]).add(edge[1]);
            neighbors.get(edge[1]).add(edge[0]);
        }

        // Find all leaves
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (neighbors.get(i).size() == 1) {
                leaves.add(i);
            }
        }

        // Trim leaves until reaching centroids
        int remainingNodes = n;
        while (remainingNodes > 2) {
            remainingNodes -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();

            for (int leaf : leaves) {
                // the only neighbor of a leaf
                int neighbor = neighbors.get(leaf).iterator().next();
                neighbors.get(neighbor).remove(leaf);
                if (neighbors.get(neighbor).size() == 1) {
                    newLeaves.add(neighbor);
                }
            }
            leaves = newLeaves;
        }

        return leaves;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int n1 = 4;
        int[][] edges1 = {{1, 0}, {1, 2}, {1, 3}};
        System.out.println(sol.findMinHeightTrees(n1, edges1).equals(Arrays.asList(1))); // true

        int n2 = 6;
        int[][] edges2 = {{3, 0}, {3, 1}, {3, 2}, {3, 4}, {5, 4}};
        System.out.println(sol.findMinHeightTrees(n2, edges2).equals(Arrays.asList(3, 4))); // true

        System.out.println("All tests passed.");
    }
}
