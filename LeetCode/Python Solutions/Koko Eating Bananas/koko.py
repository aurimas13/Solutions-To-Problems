from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    @staticmethod
    def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # create a mapping of parent to children
        parent_to_children = defaultdict(list)
        for i in range(len(pid)):
            parent_to_children[ppid[i]].append(pid[i])

        # BFS using deque
        killed_processes = []
        q = deque()
        q.append(kill)
        while q:
            current = q.popleft()
            killed_processes.append(current)
            for child in parent_to_children[current]:
                q.append(child)

        return killed_processes


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5)
    # pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5 -> [5,10]
    # pid = [1], ppid = [0], kill = 1 -> [1]
    print(Solve)