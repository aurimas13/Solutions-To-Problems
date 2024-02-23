Problem description of "Cheapest Flights Within K Stops" can be found [here](https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/) 
and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Cheapest%20Flights%20Within%20K%20Stops/cheapest.java).

To check the solution in terminal first compile Java file as `javac cheapest.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Explanation:

- **Initialization**: We start by initializing an array `dist` to store the minimum cost to reach each city from the source. All entries are initialized to `Integer.MAX_VALUE` (infinity) except for the source city, which is set to `0`.

- **Relaxation**: For each iteration (up to `k + 1`), we create a clone of the `dist` array called `newDist` to store the updated distances for this iteration. We then iterate through all flights, updating the cost to reach each destination city if a cheaper path is found using the current flight.

- **Destination Check**: After completing the iterations, we check if the destination city's cost is still infinity (`Integer.MAX_VALUE`). If it is, it means there's no path within `k` stops, and we return `-1`. Otherwise, we return the cost stored in `dist[dst]`.