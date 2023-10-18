from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Step 1: Build the graph and calculate in-degrees.
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)  # We use 1-based indexing for courses.
        
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
            
        # Step 3: Initialize the time to start each course.
        # Courses that don't have prerequisites can start immediately.
        start_time = [0] * (n + 1)
        
        # Step 2: Find courses without prerequisites.
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Step 4: Process each course, update in-degrees and start times.
        while queue:
            course = queue.popleft()
            for nextCourse in graph[course]:
                in_degree[nextCourse] -= 1
                # The time to start the next course is the completion time of the current course.
                start_time[nextCourse] = max(start_time[nextCourse], start_time[course] + time[course - 1])
                if in_degree[nextCourse] == 0:
                    queue.append(nextCourse)
                    
        # Step 5: The result is the maximum completion time.
        return max(start_time[i] + time[i - 1] for i in range(1, n + 1))
