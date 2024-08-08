class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  // East, South, West, North
        int[][] result = new int[rows * cols][2];
        int count = 0;
        result[count++] = new int[]{rStart, cStart};
        
        if (rows * cols == 1) return result;
        
        int steps = 0;
        int d = 0;  // Start facing East
        
        while (count < rows * cols) {
            if (d % 2 == 0) steps++;
            
            for (int i = 0; i < steps; i++) {
                rStart += directions[d][0];
                cStart += directions[d][1];
                if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) {
                    result[count++] = new int[]{rStart, cStart};
                }
                if (count == rows * cols) return result;
            }
            
            d = (d + 1) % 4;  // Change direction
        }
        
        return result;
    }
}