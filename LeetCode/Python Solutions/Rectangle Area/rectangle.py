class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:        
        # Calculate the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        
        # Calculate the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the overlapping area between the two rectangles
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        # Check if the two rectangles overlap
        overlap_area = max(overlap_width, 0) * max(overlap_height, 0)
        
        # Calculate the total area covered by the two rectangles
        total_area = area1 + area2 - overlap_area
        
        return total_area

# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2)  
    # ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2 -> 45
    # ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2 -> 16
    print(Solve)
