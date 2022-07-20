from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for equation, value in zip(equations, values):
            adj[equation[0]].append((equation[1], value))
            adj[equation[1]].append((equation[0], 1 / value))
        ans = []
        for query in queries:
            self.bfs(query, adj, ans)
        return ans

    def bfs(self, query, adj, ans):
        x, y = query
        queue = deque([(x, 1)])
        visited = set([x])
        while queue:
            for _ in range(len(queue)):
                node, r = queue.popleft()
                for neighbor, v in adj[node]:
                    if neighbor == y:
                        ans.append(r * v)
                        return
                    if neighbor not in visited:
                        queue.append((neighbor, r * v))
                        visited.add(neighbor)
        ans.append(-1.0)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])  # sequations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] -> [6.0,0.5,-1.0, 1.0,-1.0] | equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]] -> [3.75,0.4,5.0,0.2]
    print(Solve)


# OR

# class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     ratios = collections.defaultdict(int)
    #     neighbors = collections.defaultdict(set)
    #
    #     for eq,val in zip(equations, values):
    #         f,s = eq
    #         ratios[(f,s)] = val
    #         ratios[(s,f)] = 1/val
    #         neighbors[f].add(s)
    #         neighbors[s].add(f)
    #
    #     def find_ratio(q):
    #         f,s = q
    #         src = tuple(q)
    #         if src  in ratios:
    #             return ratios[src]
    #         visited = set()
    #         search = [f]
    #         values = [1]
    #         while search:
    #
    #             lft = search.pop(0)
    #             val = values.pop(0)
    #             if lft in visited:
    #                 continue
    #             else:
    #                 visited.add(lft)
    #                 for neigh in neighbors[lft]:
    #                     search.append(neigh)
    #                     to_append = val*ratios[(lft, neigh)]
    #                     if neigh == s:
    #                         ratios[(f, neigh)] = to_append
    #                         ratios[(neigh, f)] = 1/to_append
    #                         neighbors[f].add(neigh)
    #                         neighbors[neigh].add(f)
    #                         return to_append
    #                     values.append(to_append)
    #         return -1
    #     res = []
    #     for query in queries:
    #         res.append(find_ratio(query))
    #     return res

# OR

# class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #
    #     graph = defaultdict(defaultdict)
    #
    #     def backtrack_evaluate(curr_node, target_node, acc_product, visited):
    #         visited.add(curr_node)
    #         ret = -1.0
    #         neighbors = graph[curr_node]
    #         if target_node in neighbors:
    #             ret = acc_product * neighbors[target_node]
    #         else:
    #             for neighbor, value in neighbors.items():
    #                 if neighbor in visited:
    #                     continue
    #                 ret = backtrack_evaluate(
    #                     neighbor, target_node, acc_product * value, visited)
    #                 if ret != -1.0:
    #                     break
    #         visited.remove(curr_node)
    #         return ret
    #
    #     # Step 1). build the graph from the equations
    #     for (dividend, divisor), value in zip(equations, values):
    #         # add nodes and two edges into the graph
    #         graph[dividend][divisor] = value
    #         graph[divisor][dividend] = 1 / value
    #
    #     # Step 2). Evaluate each query via backtracking (DFS)
    #     #  by verifying if there exists a path from dividend to divisor
    #     results = []
    #     for dividend, divisor in queries:
    #         if dividend not in graph or divisor not in graph:
    #             # case 1): either node does not exist
    #             ret = -1.0
    #         elif dividend == divisor:
    #             # case 2): origin and destination are the same node
    #             ret = 1.0
    #         else:
    #             visited = set()
    #             ret = backtrack_evaluate(dividend, divisor, 1, visited)
    #         results.append(ret)
    #
    #     return results
