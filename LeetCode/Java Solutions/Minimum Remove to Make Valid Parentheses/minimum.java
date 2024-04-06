class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();
        
        // Precompute the cumulative count of 'Y's from the end
        int[] cumYs = new int[n + 1];
        cumYs[n - 1] = customers.charAt(n - 1) == 'Y' ? 1 : 0;
        for (int i = n - 2; i >= 0; i--) {
            cumYs[i] = cumYs[i + 1] + (customers.charAt(i) == 'Y' ? 1 : 0);
        }
        
        int min_penalty = cumYs[0];
        int best_hour = 0;
        int no_customers = 0;  // number of hours with 'N' before the current hour
        
        for (int i = 0; i < n; i++) {
            if (customers.charAt(i) == 'N') {
                no_customers++;
            }
            int penalty = no_customers + cumYs[i+1];
            if (penalty < min_penalty) {
                min_penalty = penalty;
                best_hour = i + 1;
            }
        }
        
        return best_hour;
    }
}
