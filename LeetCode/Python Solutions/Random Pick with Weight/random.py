from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the array of people in decreasing order of height and increasing order of k
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # initialize an empty list to store the reconstructed queue
        queue = []
        
        # insert each person in the sorted array at the kth index in the queue
        for p in people:
            queue.insert(p[1], p)
        
        return queue

