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


# Tests:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) 
    # -> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    # people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    # -> [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    print(Solve)
    