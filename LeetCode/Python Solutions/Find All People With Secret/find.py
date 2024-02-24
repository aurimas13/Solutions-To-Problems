from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Initialize the set of people who know the secret initially.
        known_set = set([0, firstPerson])
        
        # Sort meetings by their time to process in chronological order.
        meetings.sort(key=lambda x: x[2])

        # A list to hold meetings grouped by the same time.
        sorted_meetings = []
        # A set to keep track of unique meeting times we have seen.
        seen_time = set()
        
        # Group meetings by their times.
        for meeting in meetings:
            # If this meeting time hasn't been seen, add a new list for this time.
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            # Append the current meeting to the latest time group.
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        # Process each group of meetings.
        for meeting_group in sorted_meetings:
            # Set to track people who initially know the secret in this time group.
            people_know_secret = set()
            # A graph to represent connections in this time group.
            graph = defaultdict(list)
            
            # Build the graph and update initial secret holders.
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            # Use BFS to propagate the secret within this time group.
            queue = deque(people_know_secret)
        
            while queue:
                # Current person sharing the secret.
                curr = queue.popleft()
                known_set.add(curr)  # Mark the current person as knowing the secret.
                # Propagate the secret to neighbors who don't know the secret yet.
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        # Return the list of people who know the secret.
        return list(known_set)
