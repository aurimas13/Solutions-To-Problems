from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total gas is less than the total cost, then it is impossible to complete the circuit.
        if sum(gas) < sum(cost):
            return -1

        # If the total gas is greater than or equal to the total cost, then there must be a solution.
        # We can start from any station and check if we can complete the circuit.
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # If the tank is negative, then we cannot start from the current station.
            # We need to start from the next station.
            if tank < 0:
                start = i + 1
                tank = 0

        return start


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    assert solution.canCompleteCircuit([1, 4, 2], [1, 2, 4]) == -1
    assert solution.canCompleteCircuit([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3
    assert solution.canCompleteCircuit([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2
    assert solution.canCompleteCircuit([1, 1, 2, 1, 2], [1, 3, 2, 3, 1]) == 3
    assert solution.canCompleteCircuit([1, 1, 3, 5, 3, 3, 5, 5, 1, 1], [2, 3, 2, 1, 3, 5, 3, 2, 2, 1]) == 5
    assert solution.canCompleteCircuit([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2
    print("All passed")