class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a stack for storing indices of temperatures
        stack = []
        # Initialize the answer array with zeros
        answer = [0] * len(temperatures)

        # Iterate through the temperatures
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                # Pop the index and calculate the days until a warmer temperature
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)  # Push the current index onto the stack

        return answer


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    # temperatures = [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
    #  temperatures = [30,40,50,60] -> [1,1,1,0]
    print(Solve)
