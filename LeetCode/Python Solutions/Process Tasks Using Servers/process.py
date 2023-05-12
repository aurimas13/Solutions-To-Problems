import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Initialize available servers with a priority queue (heap)
        # Tuple format: (weight, index)
        available_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available_servers)
        
        # Initialize busy servers with a priority queue (heap)
        # Tuple format: (release time, weight, index)
        busy_servers = []

        # Initialize the result list
        result = []

        # Process tasks
        for time, task_duration in enumerate(tasks):
            # Release the servers that have completed their tasks
            while busy_servers and busy_servers[0][0] <= time:
                release_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, (weight, index))
            
            # Assign the task to the least weighted available server
            if available_servers:
                weight, index = heapq.heappop(available_servers)
                result.append(index)
                heapq.heappush(busy_servers, (time + task_duration, weight, index))
            else:
                # Wait for the next server to be released
                release_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(busy_servers, (release_time + task_duration, weight, index))
                result.append(index)

        return result

# Checking in Terminal/Console

if __name__ == '__main__':# Test case
    Instant = Solution()
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    Solve = Instant.assignTasks(servers, tasks) 
    # Expected output: [2, 2, 0, 2, 1, 2]
    print(Solve)
