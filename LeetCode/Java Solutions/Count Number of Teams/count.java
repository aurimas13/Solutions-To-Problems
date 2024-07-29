class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        
        for j in range(1, n - 1):
            left_smaller = sum(1 for i in range(j) if rating[i] < rating[j])
            left_larger = sum(1 for i in range(j) if rating[i] > rating[j])
            right_smaller = sum(1 for k in range(j + 1, n) if rating[k] < rating[j])
            right_larger = sum(1 for k in range(j + 1, n) if rating[k] > rating[j])
            
            result += left_smaller * right_larger + left_larger * right_smaller
        
        return result