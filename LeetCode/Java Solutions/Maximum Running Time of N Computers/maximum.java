public class Solution {
    // Function to calculate the maximum runtime for all computers
    public long maxRunTime(int numberOfComputers, int[] batteries) {
        // Calculate the total power of all batteries
        long totalBatteryPower = 0;
        for (int batteryPower : batteries) {
            totalBatteryPower += batteryPower;
        }
        
        // Set the initial search bounds for binary search
        long lowerBound = 1, upperBound = totalBatteryPower / numberOfComputers;
        
        // Perform binary search to find the maximum possible time
        while (lowerBound < upperBound) {
            // Calculate the midpoint of the current search range
            long midpointTime = (lowerBound + upperBound + 1) / 2;
            
            // Check if it's possible to run the computers for the midpoint time
            if (isTimePossible(batteries, numberOfComputers, midpointTime)) {
                // If it's possible, update the lower bound to the midpoint time
                lowerBound = midpointTime;
            } else {
                // If it's not possible, update the upper bound to one less than the midpoint time
                upperBound = midpointTime - 1;
            }
        }
        
        // Return the maximum possible time
        return lowerBound;
    }
    
    // Function to check if it's possible to run all computers for a given time
    public boolean isTimePossible(int[] batteries, int numberOfComputers, long time) {
        // Calculate the total available power for the given time
        long totalAvailablePower = 0;
        for(int batteryPower : batteries) {
            // Each battery can contribute its power or the time, whichever is smaller
            totalAvailablePower += Math.min(batteryPower, time);
        }
        
        // Check if the total available power is enough to run all computers for the given time
        return (totalAvailablePower >= (long) time * numberOfComputers);
    }
}

