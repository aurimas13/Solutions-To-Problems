public class Solution {
    public int[][] imageSmoother(int[][] img) {
        if (img == null || img.length == 0 || img[0].length == 0) {
            return new int[0][0];
        }

        int rows = img.length;
        int cols = img[0].length;
        int[][] res = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int count = 0;
                int sum = 0;

                for (int x = Math.max(0, i - 1); x < Math.min(i + 2, rows); x++) {
                    for (int y = Math.max(0, j - 1); y < Math.min(j + 2, cols); y++) {
                        sum += img[x][y];
                        count++;
                    }
                }

                res[i][j] = sum / count;
            }
        }

        return res;
    }
}
