from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # create an empty stack to store the surviving asteroids
        for new in asteroids:  # iterate over the given asteroid list
            while stack and new < 0 < stack[-1]:  # loop until we have asteroid in stack and a collision might happen
                if stack[-1] < -new:  # if the incoming asteroid is bigger, then pop the top asteroid in the stack
                    stack.pop()
                    continue  # continue to the next loop iteration
                elif stack[-1] == -new:  # if the incoming asteroid is the same size, then also pop the top asteroid
                    stack.pop()
                break  # stop the loop because the current asteroid is completely destroyed
            else:  # if the while loop was not broken, it means a new asteroid should be added to the stack
                stack.append(new)
        return stack  # return the surviving asteroids

