from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:

        volume = 0
        shift = 0

        landscape = []

        def checkSegment(l, r, arr):
            v = 0
            edge = min(r, l)
            while len(arr) > 0:
                h = arr.pop()
                if h > edge:
                    edge = h
                else:
                    v += edge - h
            return v

        for i in range(len(height)):

            if shift >= len(height):
                break

            left = height[shift]
            right = 0
            for j in range(1 + shift, len(height)):
                right = height[j]
                shift += 1
                if right >= left:
                    volume += checkSegment(left, right, landscape)
                    shift = j
                    break
                else:
                    landscape.append(right)

            if len(landscape) > 0:
                volume += checkSegment(left, right, landscape)

        return volume


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.trap(
        height=[4, 2, 0, 3, 2, 5])  # height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6 | height = [4,2,0,3,2,5] -> 9
    print(Solve)
      
