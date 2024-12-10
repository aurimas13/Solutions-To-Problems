class Solution:
   def maxTwoEvents(self, events: List[List[int]]) -> int:
       # Sort events by start time
       events.sort(key=lambda x: x[0])
       n = len(events)
       
       # Store maximum value from right for each index
       max_right = [0] * (n + 1)
       curr_max = 0
       
       for i in range(n - 1, -1, -1):
           curr_max = max(curr_max, events[i][2])
           max_right[i] = curr_max
           
       max_sum = 0
       
       # Try each event as first event
       for i, [start, end, value] in enumerate(events):
           # Binary search for non-overlapping event
           left, right = i + 1, n
           while left < right:
               mid = (left + right) // 2
               if mid < n and events[mid][0] <= end:
                   left = mid + 1
               else:
                   right = mid
                   
           # Update max_sum
           max_sum = max(max_sum, value + max_right[left] if left < n else value)
           
       return max_sum