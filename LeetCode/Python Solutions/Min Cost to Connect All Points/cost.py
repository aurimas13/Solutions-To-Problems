from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Calculate the Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Initialize the minimum spanning tree (MST) distance to 0
        total_distance = 0

        # Initialize the visited set and the priority queue
        visited = set()
        priority_queue = [(0, 0)]

        # Perform Prim's algorithm to find the MST
        while priority_queue:
            distance, point = heapq.heappop(priority_queue)
            if point not in visited:
                visited.add(point)
                total_distance += distance
                for i, next_point in enumerate(points):
                    if i not in visited:
                        heapq.heappush(priority_queue, (manhattan_distance(points[point], next_point), i))

        return total_distance

# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert solution.minCostConnectPoints(points1) == 20

    # Test case 2
    points2 = [[3, 12], [-2, 5], [-4, 1]]
    assert solution.minCostConnectPoints(points2) == 18

    # Test case 3
    points3 = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    assert solution.minCostConnectPoints(points3) == 4

    print("All test cases passed!")
