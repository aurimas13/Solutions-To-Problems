class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Initialize a list to keep track of rows
        rows = []
        
        # Count the frequency of each number
        freq = collections.Counter(nums)
        
        # Sort the numbers based on their frequency
        nums.sort(key=lambda x: -freq[x])
        
        for num in nums:
            # Check if the number can be placed in any existing row
            placed = False
            for row in rows:
                if num not in row:
                    row.append(num)
                    placed = True
                    break
            
            # If the number wasn't placed, create a new row for it
            if not placed:
                rows.append([num])
        
        return rows
