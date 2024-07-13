from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        
        for pos, health, dir, idx in robots:
            if dir == 'R':
                stack.append((pos, health, dir, idx))
            else:  # dir == 'L'
                while stack and stack[-1][2] == 'R':
                    prev_pos, prev_health, prev_dir, prev_idx = stack.pop()
                    if prev_health > health:
                        prev_health -= 1
                        health = 0
                        stack.append((prev_pos, prev_health, prev_dir, prev_idx))
                        break
                    elif prev_health < health:
                        health -= 1
                    else:  # prev_health == health
                        health = 0
                        break
                if health > 0:
                    stack.append((pos, health, dir, idx))
        
        result = sorted(stack, key=lambda x: x[3])
        return [health for pos, health, dir, idx in result]

# Example usage:
sol = Solution()
print(sol.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))  # Output: [2, 17, 9, 15, 10]
print(sol.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))     # Output: [14]
print(sol.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))     # Output: []
