from typing import List
from collections import deque


class Solution:
    @staticmethod
    def wallsAndGates(rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rooms_row, room = len(rooms), len(rooms[0])

        for i in range(rooms_row):
            for j in range(room):
                if rooms[i][j] != 0:    continue
                search_rooms = deque([(i, j, 0)])  # all the rooms
                visited = set([(i, j, 0)])  # this set keeps track of rooms you visited

                while search_rooms:
                    (rooms_row_idx, room_idx,
                     extra) = search_rooms.popleft()  # extra variable checks the distance from open room to the gate
                    for row, col in [(rooms_row_idx, room_idx + 1), (rooms_row_idx + 1, room_idx),\
                                     (rooms_row_idx, room_idx - 1), (rooms_row_idx - 1, room_idx)]:
                        if 0 <= row <= rooms_row - 1 and 0 <= col <= room - 1 \
                                and rooms[row][col] != -1 and rooms[row][col] != 0 \
                                and not (row, col) in visited:
                            search_rooms.append((row, col, extra + 1))
                            visited.add((row, col))
                            rooms[row][col] = min(extra + 1, rooms[row][col])


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.wallsAndGates(rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
                                           [2147483647,-1,2147483647,-1], [0,-1,2147483647,2147483647]])
    # rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],
    # [0,-1,2147483647,2147483647]] -> NONE yet could be [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    print(Solve) # returns None as the problem asks

