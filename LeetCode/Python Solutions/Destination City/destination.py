from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        for path in paths:
            cities.add(path[0])
        for path in paths:
            if path[1] not in cities:
                return path[1]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.destCity(paths = [["B","C"],["D","B"],["C","A"]])
    # paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] -> "Sao Paulo"
    # paths = [["B","C"],["D","B"],["C","A"]] -> "A"
    print(Solve)