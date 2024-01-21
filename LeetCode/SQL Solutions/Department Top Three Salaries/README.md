The problem description of "Department Top Three Salaries" is found [here](https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Department%20Top%20Three%20Salaries/top.sql).

**Explanation**:

`Objective`:
The main goal is to identify employees who are in the top three when it comes to earning within their respective departments.

`Approach`:
To identify these top earners, we can't simply choose the top three earners directly, because there might be employees with the same salary. That's why we use the DENSE_RANK() function which can assign the same rank to employees with equal salaries.

Using `DENSE_RANK()`:
The DENSE_RANK() function is a window function in SQL. In our context, it assigns a rank to each employee based on their salary. If two employees in the same department have the same salary, they get the same rank. This is essential for the problem since there might be scenarios where multiple top earners in a department earn the same amount.

For instance, if the top salaries in a department are 90k, 85k, 85k, and 80k, the ranks assigned will be 1, 2, 2, and 3 respectively.

`Partitioning`:
The PARTITION BY clause in the DENSE_RANK() function ensures that the ranking is reset and recalculated for each department. This way, each department gets its own set of top earners without being influenced by the salary distribution of another department.

`Joining Tables`:
We perform a JOIN between the Employee and Department tables. This is done to match each employee with their respective department and to extract the department name for our final result.

`Filtering`:
After computing the rankings, we filter out the results using the WHERE clause to only consider employees with ranks 1, 2, or 3, thus achieving the objective of fetching the top three unique earners from each department.

`Final Output`:
The final query output lists down the department name, employee name, and their corresponding salary for all those who fit the criteria of being the top three earners in their respective departments.

**Implementation**:

Imagine a large corporation with several departments - HR, IT, Sales, Marketing, Finance, and so forth. Each department has many employees with varying salaries. The corporation wants to run an incentive program where they provide special bonuses to the top three earners in each department.

The HR department, before implementing this bonus program, wants to have a list of these top earners across all departments. The above SQL solution would allow them to quickly identify these top performers. They could run this query at the end of each fiscal year to determine the high earners, and then proceed with their bonus distributions accordingly.

Additionally, having such a list is also useful for management to get insights into the salary structure across various departments. They can use this data to identify if any department is over or underpaying their top talent in comparison to others.
