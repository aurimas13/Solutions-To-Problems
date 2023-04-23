from collections import defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Initialize graph and in_degree dictionaries
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        # Create adjacency list and count incoming edges for each node
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Initialize queue and visited set
        queue = deque([u for u in range(len(colors)) if in_degree[u] == 0])
        visited = set(queue)

        # Initialize counter dictionary
        counter = [defaultdict(int) for _ in range(len(colors))]

        # BFS traversal
        while queue:
            curr = queue.popleft()
            counter[curr][colors[curr]] += 1

            # Update counter for each adjacent node and decrease in_degree
            for neighbor in graph[curr]:
                for color, count in counter[curr].items():
                    counter[neighbor][color] = max(counter[neighbor][color], count)

                in_degree[neighbor] -= 1

                # Add to the queue if the node has not been visited and has 0 incoming edges
                if neighbor not in visited and in_degree[neighbor] == 0:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # Check for cycles in the graph
        if len(visited) != len(colors):
            return -1

        # Calculate the maximum color value
        max_color_value = 0
        for node_counter in counter:
            max_color_value = max(max_color_value, max(node_counter.values()))

        return max_color_value


if __name__ == "__main__":
    solution = Solution()

    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    assert solution.largestPathValue(colors, edges) == 3

    colors = "a"
    edges = [[0, 0]]
    assert solution.largestPathValue(colors, edges) == -1
