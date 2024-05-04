from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # The lightest person is paired
            # The heaviest person always goes on the boat
            right -= 1
            boats += 1
        
        return boats
