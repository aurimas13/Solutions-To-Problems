from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Initialize an empty list to store the results
        res = []
        
        # Iterate through each pair of left and right indices
        for i in range(len(l)):
            # Extract the subarray between the left and right indices
            subarray = nums[l[i]:r[i]+1]
            
            # Sort the subarray in ascending order
            subarray.sort()
            
            # Calculate the common difference between consecutive elements
            common_diff = subarray[1] - subarray[0]
            
            # Check if the subarray is arithmetic
            is_arithmetic = True
            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j-1] != common_diff:
                    is_arithmetic = False
                    break
            
            # Append the result to the list of results
            res.append(is_arithmetic)
        
        return res


# Instantiation to check values
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])  
    # nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5] -> [true,false,true]
    # nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10] -> [false,true,false,false,true,true]
    print(Solve)
