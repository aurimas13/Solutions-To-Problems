The problem description of "Primary Department for Each Employee" can be found [here](https://leetcode.com/problems/primary-department-for-each-employee/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Percentage%20of%20Users%20Attended%20a%20Contest/percentage.sql).

**Explanation**:

1. We use a Common Table Expression (CTE) named PrimaryDepartments to calculate the count of departments for each employee using the COUNT(*) OVER(PARTITION BY employee_id) window function. This gives us the number of departments each employee belongs to.

2. In the main query, we filter out the rows based on two conditions:
If the primary_flag is 'Y', then we select that department.
If an employee belongs to only one department (dept_count = 1) and the primary_flag is 'N', then we select that department.

3. We don't select employees who belong to multiple departments and don't have a primary department.