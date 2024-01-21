import java.util.Stack;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();  // create an empty stack to store the surviving asteroids
        for (int i = 0; i < asteroids.length; i++) {  // iterate over the given asteroid array
            if (asteroids[i] > 0)  // if the asteroid is moving right, just push it into the stack
                stack.push(asteroids[i]);
            else {  // else, it's moving left
                while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(asteroids[i])) { 
                    // loop until we have asteroid in stack and a collision might happen
                    // and the last asteroid is smaller
                    stack.pop();  // destroy the smaller asteroid
                }
                if (!stack.isEmpty() && stack.peek() == Math.abs(asteroids[i])) 
                    // if the incoming asteroid is the same size, destroy both
                    stack.pop();
                else if (stack.isEmpty() || stack.peek() < 0)
                    // if there are no more asteroids or the last asteroid is also moving left
                    stack.push(asteroids[i]);  // push the current asteroid to the stack
            }
        }

        // Convert stack to array
        int[] survivingAsteroids = new int[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            survivingAsteroids[i] = stack.pop();
        }
        return survivingAsteroids;  // return the surviving asteroids
    }
}

