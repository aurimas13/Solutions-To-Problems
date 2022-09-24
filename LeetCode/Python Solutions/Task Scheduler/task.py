from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequencies = self.tasksToDic(tasks, {})
        max_heap = []
        for value in task_frequencies.values():
            heapq.heappush(max_heap, -1 * value)
        max_frequency = -1 * heapq.heappop(max_heap)
        max_idle_time = (max_frequency - 1) * n
        while max_heap:
            max_idle_time -= min(max_frequency - 1, -1 * heapq.heappop(max_heap))
        max_idle_time = max(max_idle_time, 0)
        return len(tasks) + max_idle_time

    def tasksToDic(self, tasks, dic):
        for task in tasks:
            if task not in dic:
                dic[task] = 1
            else:
                dic[task] += 1
        return dic


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2) # tasks = ["A","A","A","B","B","B"], n = 2 -> 8 | tasks = ["A","A","A","B","B","B"], n = 0 -> 6
    print(Solve)
