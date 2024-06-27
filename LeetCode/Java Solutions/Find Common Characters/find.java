class Solution {
    public int findCenter(int[][] edges) {
        // Since it's a star graph, the center node must appear in the first two edges
        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {
            return edges[0][0];
        }
        return edges[0][1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findCenter(new int[][]{{1, 2}, {2, 3}, {4, 2}}));  // Output: 2
        System.out.println(sol.findCenter(new int[][]{{1, 2}, {5, 1}, {1, 3}, {1, 4}}));  // Output: 1
    }
}
