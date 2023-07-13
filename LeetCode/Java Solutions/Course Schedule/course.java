import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Define an adjacency list
        List<Integer>[] adj_list = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++)
            adj_list[i] = new ArrayList<Integer>();
        // Define a visit list, 0 means unvisited, 1 means being visited, 2 means completely visited
        int[] visit = new int[numCourses];
        
        // Convert edge list to adjacency list
        for (int[] edge : prerequisites)
            adj_list[edge[0]].add(edge[1]);
        
        // Do DFS from each node
        for (int i = 0; i < numCourses; i++) {
            if (visit[i] == 0 && !dfs(i, adj_list, visit))
                return false;
        }
        return true;
    }

    // Helper function to do DFS
    private boolean dfs(int i, List<Integer>[] adj_list, int[] visit) {
        // If it is being visited, then we have a cycle, thus return false
        if (visit[i] == 1)
            return false;
        // If it is done visited, then do not visit again
        if (visit[i] == 2)
            return true;
        
        // Mark as being visited
        visit[i] = 1;
        // Visit all the neighbours
        for (int j : adj_list[i]) {
            if (!dfs(j, adj_list, visit))
                return false;
        }
        // After visit all the neighbours, mark it as done visited
        visit[i] = 2;
        return true;
    }
}
