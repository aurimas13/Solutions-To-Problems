from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into a list of tuples
        people = list(zip(names, heights))
        # Sort the list of tuples by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        # Extract and return the sorted names
        return [person[0] for person in people]

# Example usage:
sol = Solution()
print(sol.sortPeople(["Mary","John","Emma"], [180,165,170]))  # Output: ["Mary", "Emma", "John"]
print(sol.sortPeople(["Alice","Bob","Bob"], [155,185,150]))   # Output: ["Bob", "Alice", "Bob"]
