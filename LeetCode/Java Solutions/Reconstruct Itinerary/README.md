The problem description of "Reconstruct Itinerary" is found [here](https://leetcode.com/problems/reconstruct-itinerary/description/?envType=daily-question&envId=2023-09-14) while the solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Reconstruct%20Itinerary/reconstruct.java).

**Explanation**:

1. Step 1: Graph Creation
`Why a Graph?`: The problem describes airports (denoted by strings) and flights between them. Each flight from one airport to another can be seen as a directed edge from one node to another in a graph.

`HashMap with Priority Queue`: We'll create a graph where each node (airport) has its neighbors (possible next destinations) stored in a priority queue (or min-heap). Why priority queue? Because if there are multiple destinations possible from an airport, we need to choose the lexicographically smallest one (as per the problem). A priority queue provides us with the smallest element in constant time.

`Graph Construction`:

Initialize a HashMap. Key is a string representing an airport, and the Value is a priority queue holding neighboring airports.
Loop through the given tickets. For each ticket:
Add the destination airport to the source airport's priority queue in the HashMap.

2. Step 2: Depth First Search (DFS)
`Starting Point`: Begin DFS from the "JFK" airport as given.

`DFS Process`:

At each airport (while it has unvisited neighbors):
Choose the next unvisited airport which is lexicographically smallest (this is provided by the priority queue in constant time).
Mark this neighboring airport as visited (in our case, pop it out from the priority queue).
Recursively perform DFS on this chosen airport.

`Dead-End or Leaf Node`: If you reach an airport which has no unvisited neighbors left, this means it's an endpoint in the current path.

3. Step 3: Backtracking and Path Construction

`Backtracking`: Once you hit a dead-end (an airport with no unvisited neighbors), backtrack. This means you'll go back to the previous airport and explore its other neighbors (if any).

`Constructing the Path`:

Every time you hit a dead-end, add the current airport to the path.
As you backtrack, keep adding the airports to the path.
Essentially, the path is constructed in a post-order manner: visiting all destinations from an airport before adding the airport itself to the path.
Reverse the Path: Since the path is constructed in reverse (from the end to the start), you must reverse the path before returning it.

4. Step 4: Return the Path

Once DFS completes, reverse the constructed path and return it as the final itinerary.

**Implementation**:

Think of a travel planner app where a user inputs all the tickets they've bought and wants to figure out the best route to travel so that all tickets are utilized.

Another use case could be in software development where you have a list of tasks (some dependent on others, some independent) and you want to find out the sequence of tasks to perform such that the ones with higher priority (or lexicographical order) are executed before the others. This approach could be used to deduce the correct sequence to perform the tasks.