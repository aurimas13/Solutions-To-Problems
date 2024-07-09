class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currentTime = 0
        totalWaitingTime = 0
        
        for arrival, time in customers:
            currentTime = max(currentTime, arrival) + time
            totalWaitingTime += currentTime - arrival
        
        return totalWaitingTime / len(customers)
