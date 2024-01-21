from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Initialize a dictionary to keep track of the current members of each group size
        groups = {}
        result = []
        
        # Iterate over the groupSizes list along with the indices
        for idx, size in enumerate(groupSizes):
            # For each group size, add the current index to the corresponding list in the dictionary
            if size not in groups:
                groups[size] = []
            groups[size].append(idx)
            
            # If the size of the list in the dictionary equals the group size
            if len(groups[size]) == size:
                # Add this list to the result
                result.append(groups[size])
                # Reset the list in the dictionary
                groups[size] = []
        
        return result
