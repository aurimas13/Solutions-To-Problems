The problem description of "The Number of Employees Which Report to Each Employee" is found [here](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/The%20Number%20of%20Employees%20Which%20Report%20to%20Each%20Employee/number.sql).

**Explanation**:

1. We're using an INNER JOIN to join the Employees table with itself. e1 represents the managers and e2 represents the employees reporting to the managers.

2. The join condition is e1.employee_id = e2.reports_to, which matches each manager with the employees that report to them.

3. The COUNT(e2.employee_id) function counts the number of employees that report to each manager.

4. The ROUND(AVG(e2.age)) function calculates the average age of the employees reporting to each manager and rounds it to the nearest integer.

5. We're grouping by e1.employee_id and e1.name to get the count and average age for each manager.

6. The HAVING reports_count >= 1 condition ensures that we only include managers who have at least one employee reporting to them in the result.

7. Finally, we're ordering the result by e1.employee_id to get the output in the order of employee IDs.