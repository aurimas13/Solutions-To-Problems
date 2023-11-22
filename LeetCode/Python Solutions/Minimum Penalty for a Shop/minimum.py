 class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Precompute the cumulative count of 'Y's from the end
        cumYs = [0] * (n + 1)
        cumYs[n - 1] = 1 if customers[-1] == 'Y' else 0
        for i in range(n - 2, -1, -1):
            cumYs[i] = cumYs[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        min_penalty = cumYs[0]
        best_hour = 0
        no_customers = 0  # number of hours with 'N' before the current hour
        
        for i in range(n):
            if customers[i] == 'N':
                no_customers += 1
            penalty = no_customers + cumYs[i+1]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
                
        return best_hour
