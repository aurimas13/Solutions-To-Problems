import java.util.*;

class Solution {
    public int shortestPathAllKeys(String[] grid) {
        // Get dimensions of the grid
        int m = grid.length;
        int n = grid[0].length();
        
        // Initialize starting position and bitmask for all keys
        int[] start = null;
        int allKeys = 0;
        
        // Find the starting position '@' and set the bitmask for all keys
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = grid[i].charAt(j);
                // If it isthe starting position, store it in 'start'
                if (c == '@') {
                    start = new int[]{i, j};
                }
                // If it is a key, add its bit representation to 'allKeys'
                else if (c >= 'a' && c <= 'f') {
                    allKeys |= 1 << (c - 'a');
                }
            }
        }
        
        // Initialize a queue for BFS with initial position, keys bitmask and steps
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{start[0], start[1], 0, 0});
        
        // Set to store visited positions with keys bitmask
        Set<String> visited = new HashSet<>();
        visited.add(start[0] + "," + start[1] + ",0");
        
        // Perform BFS
        while (!queue.isEmpty()) {
            // Dequeue the current position, keys bitmask and steps
            int[] current = queue.poll();
            int x = current[0], y = current[1], keys = current[2], steps = current[3];
            
            // If we have collected all keys, return the steps
            if (keys == allKeys) {
                return steps;
            }
            
            // Explore all 4 neighboring cells
            int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                
                // Continue if next position is in grid and not a wall
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx].charAt(ny) != '#') {
                    char nc = grid[nx].charAt(ny);
                    
                    // If it is a locked door and we don't have the key, skip
                    if (nc >= 'A' && nc <= 'F' && (keys & (1 << (nc - 'A'))) == 0) {
                        continue;
                    }
                    
                    // If it is a key, add its bit representation to 'keys'
                    int nkeys = keys;
                    if (nc >= 'a' && nc <= 'f') {
                        nkeys = keys | (1 << (nc - 'a'));
                    }
                    
                    // If this state hasn't been visited, add it to the queue and visited set
                    String state = nx + "," + ny + "," + nkeys;
                    if (!visited.contains(state)) {
                        visited.add(state);
                        queue.offer(new int[]{nx, ny, nkeys, steps + 1});
                    }
                }
            }
        }
        
        // If we reach here, it means it is not possible to collect all keys
        return -1;
    }
}
