from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Given a list of bus routes, where routes[i] is a bus route that the ith 
        bus repeats forever, and a starting bus stop source and a destination 
        bus stop target, return the least number of buses we must take to reach 
        the destination bus stop. If it is not possible to reach the target 
        bus stop, return -1.
        
        :param routes: A list of lists of integers representing the bus routes.
        :param source: An integer representing the starting bus stop.
        :param target: An integer representing the destination bus stop.
        :return: An integer representing the least number of buses we must take 
                 to reach the destination bus stop.
        """

        if source == target:
            return 0

        # Create a mapping between each bus stop and the bus routes that pass through them
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        # Perform a breadth-first search on the bus stop graph to find the shortest path to the destination bus stop
        visited_stops = {source}
        visited_routes = set()
        queue = deque([(source, 0)])

        while queue:
            current_stop, depth = queue.popleft()

            for route_index in stop_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop == target:
                            return depth + 1
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, depth + 1))

        return -1


# Tests
if __name__ == "__main__":
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
    assert Solution().numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12) == -1
    assert Solution().numBusesToDestination([[1, 7], [3, 5]], 5, 5) == 0
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2

    print("Passed all tests!")