from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        queue = deque([("0000", 0)])  # (state, depth)
        visited = set(["0000"])
        
        while queue:
            state, depth = queue.popleft()
            
            if state == target:
                return depth
            
            for i in range(4):
                digit = int(state[i])
                # Generate the next and previous digit for each wheel
                for move in [-1, 1]:
                    next_digit = (digit + move) % 10
                    next_state = state[:i] + str(next_digit) + state[i+1:]
                    
                    if next_state not in visited and next_state not in dead_set:
                        visited.add(next_state)
                        queue.append((next_state, depth + 1))
        
        return -1
