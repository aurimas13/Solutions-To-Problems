import java.util.*;

class Solution {
    // Helper function to calculate the Manhattan distance between two points
    private int manhattanDistance(int[] p1, int[] p2) {
        return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
    }

    public int minCostConnectPoints(int[][] points) {
        // Initialize the minimum spanning tree (MST) distance to 0
        int totalDistance = 0;

        // Initialize the visited set and the priority queue
        Set<Integer> visited = new HashSet<>();
        PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        priorityQueue.offer(new int[] {0, 0});

        // Perform Prim's algorithm to find the MST
        while (!priorityQueue.isEmpty()) {
            int[] curr = priorityQueue.poll();
            int distance = curr[0], point = curr[1];
            
            if (!visited.contains(point)) {
                visited.add(point);
                totalDistance += distance;

                for (int i = 0; i < points.length; i++) {
                    if (!visited.contains(i)) {
                        priorityQueue.offer(new int[] {manhattanDistance(points[point], points[i]), i});
                    }
                }
            }
        }
        return totalDistance;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        int[][] points1 = {{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}};
        assert solution.minCostConnectPoints(points1) == 20;

        // Test case 2
        int[][] points2 = {{3, 12}, {-2, 5}, {-4, 1}};
        assert solution.minCostConnectPoints(points2) == 18;

        // Test case 3
        int[][] points3 = {{0, 0}, {1, 1}, {1, 0}, {-1, 1}};
        assert solution.minCostConnectPoints(points3) == 4;

        System.out.println("All test cases passed!");
    }
}
