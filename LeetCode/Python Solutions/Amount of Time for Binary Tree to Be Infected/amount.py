
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Convert tree to graph
        graph = collections.defaultdict(list)
        def buildGraph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                if node.left:
                    graph[node.val].append(node.left.val)
                    buildGraph(node.left, node)
                if node.right:
                    graph[node.val].append(node.right.val)
                    buildGraph(node.right, node)
        buildGraph(root, None)

        # BFS to simulate infection spread
        visited = set()
        queue = collections.deque([(start, 0)])
        maxTime = 0
        while queue:
            node, time = queue.popleft()
            if node not in visited:
                visited.add(node)
                maxTime = max(maxTime, time)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, time + 1))
        
        return maxTime
