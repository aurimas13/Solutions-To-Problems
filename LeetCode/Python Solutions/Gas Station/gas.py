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
    assert Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert Solution().canCompleteCircuit([2,3,4], [3,4,3]) == -1  
    assert Solution().canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]) == 4
    print("All passed")