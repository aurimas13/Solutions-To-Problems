import java.util.*;

class Solution {
    public int equalPairs(int[][] grid) {
        int[] row = new int[grid.length];
        int[] col = new int[grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
            row[i] += grid[i][j];
            col[j] += grid[i][j];
            }
        }
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
            res = Math.max(res, Math.abs(row[i] - col[j]));
            }
        }
        return res;
        }
    }