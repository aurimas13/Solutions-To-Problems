import java.util.*;

class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n];
        int[] inDegree = new int[n];
        List<Set<Integer>> ancestors = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
            ancestors.add(new HashSet<>());
        }
        
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            inDegree[edge[1]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        List<Integer> topoOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topoOrder.add(node);
            for (int neighbor : graph[node]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        for (int node : topoOrder) {
            for (int neighbor : graph[node]) {
                ancestors.get(neighbor).add(node);
                ancestors.get(neighbor).addAll(ancestors.get(node));
            }
        }
        
        List<List<Integer>> result = new ArrayList<>();
        for (Set<Integer> ancestorSet : ancestors) {
            List<Integer> sortedAncestors = new ArrayList<>(ancestorSet);
            Collections.sort(sortedAncestors);
            result.add(sortedAncestors);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getAncestors(8, new int[][]{{0,3},{0,4},{1,3},{2,4},{2,7},{3,5},{3,6},{3,7},{4,6}}));
        System.out.println(sol.getAncestors(5, new int[][]{{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}));
    }
}
