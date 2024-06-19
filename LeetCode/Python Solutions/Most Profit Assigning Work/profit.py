class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into pairs and sort them by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their abilities
        worker.sort()
        
        total_profit = 0
        max_profit = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit

# Example usage:
s = Solution()
print(s.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))  # Output: 100
print(s.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))  # Output: 0
