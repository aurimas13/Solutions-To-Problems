from typing import List


class Solution:
    INF = int(2e9)

    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        # Step 1: Compute the initial shortest distance from source to destination
        current_shortest_distance = self.run_dijkstra(
            edges, n, source, destination
        )

        # If the current shortest distance is less than the target, return an empty result
        if current_shortest_distance < target:
            return []
        matches_target = current_shortest_distance == target

        # Step 2: Iterate through each edge to adjust its weight if necessary
        for edge in edges:
            # Skip edges that already have a positive weight
            if edge[2] > 0:
                continue

            # Set edge weight to a large value if current distance matches target, else set to 1
            edge[2] = self.INF if matches_target else 1

            # Step 3: If current shortest distance does not match target
            if not matches_target:
                # Compute the new shortest distance with the updated edge weight
                new_distance = self.run_dijkstra(edges, n, source, destination)
                # If the new distance is within the target range, update edge weight to match target
                if new_distance <= target:
                    matches_target = True
                    edge[2] += target - new_distance

        # Return modified edges if the target distance is achieved, otherwise return an empty result
        return edges if matches_target else []

    def run_dijkstra(
        self, edges: List[List[int]], n: int, source: int, destination: int
    ) -> int:
        # Step 1: Initialize adjacency matrix and distance arrays
        adj_matrix = [[self.INF] * n for _ in range(n)]
        min_distance = [self.INF] * n
        visited = [False] * n

        # Set the distance to the source node as 0
        min_distance[source] = 0

        # Step 2: Fill the adjacency matrix with edge weights
        for nodeA, nodeB, weight in edges:
            if weight != -1:
                adj_matrix[nodeA][nodeB] = weight
                adj_matrix[nodeB][nodeA] = weight

        # Step 3: Perform Dijkstra's algorithm
        for _ in range(n):
            # Find the nearest unvisited node
            nearest_unvisited_node = -1
            for i in range(n):
                if not visited[i] and (
                    nearest_unvisited_node == -1
                    or min_distance[i] < min_distance[nearest_unvisited_node]
                ):
                    nearest_unvisited_node = i

            # Mark the nearest node as visited
            visited[nearest_unvisited_node] = True

            # Update the minimum distance for each adjacent node
            for v in range(n):
                min_distance[v] = min(
                    min_distance[v],
                    min_distance[nearest_unvisited_node]
                    + adj_matrix[nearest_unvisited_node][v],
                )
        # Return the shortest distance to the destination node
        return min_distance[destination]