The problem description of "Find All People With Secret" is found [here](https://leetcode.com/problems/find-all-people-with-secret/) while the solution can be found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Find%20All%20People%20With%20Secret/find.java).

To check the solution in terminal first compile Java file as `javac find.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

**Explanation**:

1. **Initialize knownSet**: A set to keep track of people who know the secret initially including person 0 and `firstPerson`.

2. **Sort meetings by Time**: The meetings are sorted based on their time to ensure we process the secret sharing in chronological order.

3. **Group Meetings by Time**: We create a list of lists (sortedMeetings) to hold groups of meetings that occur at the same time. This allows us to process all meetings happening simultaneously together.

4. **Build Graph and Propagate Secret**: For each group of meetings, we build a graph representing the connections between people. Then, we perform a Breadth-First Search (BFS) starting from the people who already know the secret, propagating the secret to their neighbors.

5. **BFS to Share Secret**: The BFS ensures that the secret is shared with everyone connected in the graph for the current time step, simulating the instantaneous sharing of the secret.

6. **Return Result**: Finally, the set of people who know the secret (`knownSet`) is converted to a list and returned.