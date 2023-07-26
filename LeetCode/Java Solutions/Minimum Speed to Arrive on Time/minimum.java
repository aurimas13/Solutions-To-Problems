public class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        // Initialize the low and high speed
        // low speed = 1 and high speed is maximum distance multiply by 10^7 to ensure cover maximum possible speed
        int low = 1, high = (int)1e7;
        for (int d : dist) high = Math.max(high, d);
        
        // If number of trains is greater than hour and hour is not integer
        // Then it's impossible to reach at time.
        if (Math.ceil(hour) < dist.length) return -1;
        
        // Binary search for minimum speed
        while (low < high) {
            int mid = (low + high) / 2;  // Find the middle speed
            double time = 0.0;  // Initialize the time with 0
            for (int i = 0; i < dist.length; i++) {  // Calculate the total time with middle speed
                if (i != dist.length - 1) time += Math.ceil(1.0 * dist[i] / mid);
                else time += 1.0 * dist[i] / mid;
            }
            if (time > hour) low = mid + 1;  // If the total time is more than given hour then increase the low speed
            else high = mid;  // Else reduce the high speed
        }
        return low;
    }
}

