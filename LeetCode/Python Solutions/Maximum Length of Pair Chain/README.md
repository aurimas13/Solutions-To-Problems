The problem of "Maximum Length of Pair Chain" can be found [here](https://leetcode.com/problems/maximum-length-of-pair-chain/description/) while the solution [here]().

**Explanation**:

To find the longest possible chain, we can use a greedy approach. The idea is to select pairs in such a way that we leave as much room as possible for subsequent pairs.

*Sorting*

The first step in the solution is to sort the pairs based on their second element (end value). Sorting helps in the greedy selection of pairs. We prioritize pairs that end earlier since they leave more space for subsequent pairs to be chained.

*Greedy Selection*

Starting from the earliest ending pair, we check if a pair can be added to the chain. If its starting value is greater than the end value of the last pair in our chain, it can be added. We then update our "current end" to be the end value of this pair and move on.

**Implementation**:

Let's think of a conference with several sessions. Each session is represented by a pair, where the first number is the start time and the second number is the end time. You want to attend as many sessions as possible, but you can't be in two places at once. How do you maximize the number of sessions you attend?

Example:
Sessions = `[[9,10], [10,11], [11,12], [10,12]]`

If you decide to attend the session from 10 to 12, you won't be able to attend the sessions from 10 to 11 and 11 to 12. So even though the session from 10 to 12 is longer, it's not optimal if you want to maximize the number of sessions.

By sorting sessions by their end times, you can make decisions that leave as much time open as possible for subsequent sessions.

For the above example, our sorted sessions are:

`[[9,10], [10,11], [11,12], [10,12]]`

Here's a potential schedule:

1. Attend the session from 9 to 10.
2. Attend the session from 10 to 11.
3. Attend the session from 11 to 12.

You have now attended 3 sessions, which is the maximum possible for the given schedule. This is essentially the same approach we use to form the longest chain of pairs.