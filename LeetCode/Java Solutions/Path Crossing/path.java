import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isPathCrossing(String path) {
        // Initialize the starting point and the set of visited points.
        int x = 0, y = 0;
        Set<String> visited = new HashSet<>();
        visited.add(x + "," + y);

        for (char move : path.toCharArray()) {
            // Update the coordinates based on the direction.
            if (move == 'N') y++;
            else if (move == 'S') y--;
            else if (move == 'E') x++;
            else if (move == 'W') x--;

            // Create a string representation of the current coordinate.
            String coord = x + "," + y;

            // Check if the new position has already been visited.
            if (visited.contains(coord)) {
                return true;
            }

            // Mark the new position as visited.
            visited.add(coord);
        }

        // The path does not cross itself.
        return false;
    }
}
