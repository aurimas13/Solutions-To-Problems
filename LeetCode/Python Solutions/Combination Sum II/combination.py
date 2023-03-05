from typing import List
import collections
import copy


class Solution:
    def dfs(self, target: int, path: List[int], recorder: dict):
        """
        Recursive function that performs DFS to find all unique combinations that sum to target
        """
        if target == 0:
            self.result_set.append(path)  # If the target is achieved, add the path to the result set
        else:
            for key in recorder:
                # Check if the number is available and can be used to achieve the target
                if recorder[key] > 0 and target - key >= 0:
                    # Create a copy of the recorder to avoid mutation
                    recorder_copy = copy.copy(recorder)
                    # Update the copy of the recorder
                    recorder[key] = 0
                    recorder_copy[key] -= 1
                    # Recursively call the DFS function
                    self.dfs(target - key, path + [key], recorder_copy)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to target
        Each number in candidates may only be used once in the combination
        Note: The solution set must not contain duplicate combinations
        """
        recorder = collections.Counter(candidates) # Use Counter to create a dictionary of candidate numbers with their frequency
        self.result_set = []
        self.dfs(target, [], recorder) # Call the DFS function to find all unique combinations
        return self.result_set


# Checking in Terminal/Console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
    # candidates = [10,1,2,7,6,1,5], target = 8
    # candidates = [2,5,2,1,2], target = 5
    print(Solve)
