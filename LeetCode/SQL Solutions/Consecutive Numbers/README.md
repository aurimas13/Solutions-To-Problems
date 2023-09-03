The problem decription of "Consecutive Numbers" can be found [here](https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is found [here]().

**Explanation**:

1. We're joining the Logs table with itself based on the id column. l2 represents the row immediately after l1, and l3 represents the row two positions after l1.

2. The WHERE clause checks if the num value of the three consecutive rows is the same.

3. We use DISTINCT to ensure that we don't have duplicate numbers in the result.

**Implementation**:

Imagine a system that logs user activities, and each activity is represented by a number. For instance, 1 might represent a login action, 2 might represent a logout action, etc. If we notice that a user is repeatedly performing the same action consecutively (e.g., trying to login multiple times in a row), it might indicate a potential issue, such as a user forgetting their password or a bot trying to brute-force its way into an account. Using the above SQL query, we can quickly identify such repetitive patterns and take appropriate actions, like sending a password reset email or blocking the IP address for a certain duration.