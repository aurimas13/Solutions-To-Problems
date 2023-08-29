The problem description of "Rising Temperature" is found [here](https://leetcode.com/problems/rising-temperature/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Rising%20Temperature/rising.sql).

**Explanation**

- We're using a self-join on the `Weather` table. `w1` represents the "previous day" and `w2` represents the "current day".
- The **DATEDIFF** function checks for rows where `w2.recordDate` is exactly one day ahead of `w1.recordDate`.
- The **WHERE** clause filters the result such that we only get rows where `w2` has a higher temperature than `w1`.

**Practical Implementation**

Imagine you're working with a climate research agency. They store daily temperature recordings in a database. To detect sudden temperature rises, which could indicate global warming effects or other climatic changes, the researchers want to know all the dates when the temperature was higher than the day before. Using the above SQL query, you can quickly provide them with this data.