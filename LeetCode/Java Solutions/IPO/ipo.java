import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        // Pair projects with their capital requirements and profits
        int n = profits.length;
        int[][] projects = new int[n][2];
        for (int i = 0; i < n; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }

        // Sort projects by their capital requirements
        Arrays.sort(projects, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        int projectIndex = 0;

        for (int i = 0; i < k; i++) {
            // Push all projects that can be started with the current capital into the heap
            while (projectIndex < n && projects[projectIndex][0] <= w) {
                maxHeap.add(projects[projectIndex][1]);
                projectIndex += 1;
            }

            // If there are no projects that can be started, break out
            if (maxHeap.isEmpty()) {
                break;
            }

            // Pop the project with the maximum profit
            w += maxHeap.poll();
        }

        return w;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int k = 2;
        int w = 0;
        int[] profits = {1, 2, 3};
        int[] capital = {0, 1, 1};
        System.out.println(sol.findMaximizedCapital(k, w, profits, capital));  // Output: 4
    }
}
