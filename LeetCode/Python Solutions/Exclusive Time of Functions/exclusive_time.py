from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_times = [0] * n
        prev_time = 0
        for log in logs:
            fn_id, event, timestamp = log.split(":")
            fn_id = int(fn_id)
            timestamp = int(timestamp)
            
            if event == "start":
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return exclusive_times

        
        
# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"])
    # n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"] -> [3,4]
    # n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"] -> [8]
    print(Solve)
