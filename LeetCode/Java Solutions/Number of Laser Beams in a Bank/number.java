class Solution {
    public int numberOfBeams(String[] bank) {
        int[] deviceCounts = new int[bank.length];
        int deviceRow = 0;  // Count of rows with devices

        // Count the number of devices in each row
        for (String row : bank) {
            for (char c : row.toCharArray()) {
                if (c == '1') {
                    deviceCounts[deviceRow]++;
                }
            }
            if (deviceCounts[deviceRow] > 0) {
                deviceRow++;
            }
        }

        // Calculate the number of beams
        int beams = 0;
        for (int i = 0; i < deviceRow - 1; i++) {
            beams += deviceCounts[i] * deviceCounts[i + 1];
        }

        return beams;
    }
}
