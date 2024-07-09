class Solution {
    public double averageWaitingTime(int[][] customers) {
        int currentTime = 0;
        long totalWaitingTime = 0;
        
        for (int[] customer : customers) {
            int arrival = customer[0];
            int time = customer[1];
            currentTime = Math.max(currentTime, arrival) + time;
            totalWaitingTime += currentTime - arrival;
        }
        
        return (double) totalWaitingTime / customers.length;
    }
}
