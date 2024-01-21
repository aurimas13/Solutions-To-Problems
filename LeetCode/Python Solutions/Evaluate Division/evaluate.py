from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize the adjacency list to represent the graph
        adj = defaultdict(list)

        # Fill up the adjacency list. For each equation "a / b = value",
        # we represent it in the graph as "a" -> "b" and "b" -> "a" with respective values
        for equation, value in zip(equations, values):
            adj[equation[0]].append((equation[1], value))
            adj[equation[1]].append((equation[0], 1 / value))

        # Prepare the list to store results of queries
        ans = []

        # Perform a BFS for each query to find the result, if possible
        for query in queries:
            self.bfs(query, adj, ans)
        
        return ans

    def bfs(self, query, adj, ans):
        # Unpack the query
        x, y = query

        # Initialize the queue with the start node and its value
        queue = deque([(x, 1)])

        # Create a set to store visited nodes
        visited = set([x])

        # While the queue is not empty
        while queue:
            # Dequeue a node and its value
            node, r = queue.popleft()

            # Visit each neighbor of the current node
            for neighbor, v in adj[node]:
                # If we've reached the end node of the query, append the result and return
                if neighbor == y:
                    ans.append(r * v)
                    return

                # If the neighbor has not been visited, enqueue it with its value
                if neighbor not in visited:
                    queue.append((neighbor, r * v))
                    visited.add(neighbor)

        # If we've exhausted all nodes and haven't found the end node, append -1.0 as the result
        ans.append(-1.0)


# Tests
if __name__ == '__main__':
    Sol = Solution()
    
    # Original Test Cases
    Solve = Sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])  
    print(Solve)  # Expected: [3.75,0.4,5.0,0.2]

    # Additional Test Cases
    Solve = Sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    print(Solve)  # Expected: [6.0,0.5,-1.0, 1.0,-1.0]

    Solve = Sol.calcEquation(equations = [["a","b"],["b","c"], ["c", "a"]], values = [2.0,3.0, 0.5], queries = [["a","c"],["b","a"],["a","a"],["b","b"],["c","c"]])
    print(Solve)  # Expected: [1.5, 0.5, 1.0, 1.0, 1.0]

    Solve = Sol.calcEquation(equations = [["x","y"], ["y","z"], ["z","x"]], values = [3.0, 2.0, 0.5], queries = [["x","z"],["z","y"],["y","x"],["x","x"],["y","y"],["z","z"]])
    print(Solve)  # Expected: [1.5, 1.5, 2.0, 1.0, 1.0, 1.0]

    # Test cases with disconnected components
    Solve = Sol.calcEquation(equations = [["a","b"],["b","c"], ["d","e"], ["e", "f"]], values = [2.0,3.0, 4.0, 5.0], queries = [["a","c"],["b","a"],["a","e"],["d","f"],["a","a"],["b","b"],["c","c"], ["d","d"], ["e","e"], ["f","f"]])
    print(Solve)  # Expected: [6.0, 0.5, -1.0, 20.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

