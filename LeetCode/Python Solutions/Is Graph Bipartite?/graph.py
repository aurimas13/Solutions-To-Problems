from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Create a color list with the size of the graph initialized with zeros (indicating no color assigned yet)
        color = [0]*len(graph)
        
        # Try to color each node in the graph
        for i in range(len(graph)):
            # If the node has not been colored yet and we can't color it validly, return False
            if color[i] == 0 and not self.valid_color(graph, 1, i, color):
                return False
        # If we can color all the nodes, return True
        return True
    
    def valid_color(self, graph, color_to_be_assigned, node, color):
        # If the node has already been colored, check if the color is the same as the color to be assigned
        if color[node] != 0:
            return color[node] == color_to_be_assigned
        # Assign the color to the node
        color[node] = color_to_be_assigned
        
        # Try to color all the adjacent nodes with the opposite color
        # If we can't color an adjacent node validly, return False
        return all(self.valid_color(graph, -color_to_be_assigned, adj_node, color) for adj_node in graph[node])


if __name__ == "__main__":
    s = Solution()

    graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
    assert not s.isBipartite(graph1), "Test case 1 failed"

    graph2 = [[1,3],[0,2],[1,3],[0,2]]
    assert s.isBipartite(graph2), "Test case 2 failed"

    print("All test cases passed!")

