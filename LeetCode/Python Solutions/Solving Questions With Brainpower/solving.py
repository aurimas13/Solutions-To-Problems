from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Length of the questions
        n = len(questions)  
        
        # Maximum number of questions to skip
        max_skip = max(question[1] for question in questions)     
        
        # Initialize the dp array with 0s, add max_skip extra slots for padding (to avoid index out of bound)
        dp = [0] * (n + max_skip + 1)
        
        # Reverse iterate through the questions
        for i in range(n - 1, -1, -1):
            # Calculate the maximum points if we solve the question
            solve = questions[i][0] + dp[i + questions[i][1] + 1]
            
            # Calculate the maximum points if we skip the question
            skip = dp[i + 1]
            
            dp[i] = max(solve, skip)
        
        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    assert sol.mostPoints([[3,2],[4,3],[4,4],[2,5]]) == 5
    assert sol.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]) == 7
    print("All tests passed!")
