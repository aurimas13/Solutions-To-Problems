The problem description of "Managers with at Least 5 Direct Reports" is found [here](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Managers%20with%20at%20Least%205%20Direct%20Reports/managers.sql).

**Explanation**:
1. `Subquery (m)`:

```sql
Copy code
SELECT managerId
FROM Employee
WHERE managerId IS NOT NULL
GROUP BY managerId
HAVING COUNT(id) >= 5
```
- **Purpose**: This subquery is designed to retrieve the managerIds of those managers who have at least 5 direct reports.
- **WHERE managerId IS NOT NULL**: Filters out rows where there is no manager.
- **GROUP BY managerId**: Groups the table by the manager ID. This allows us to count the number of direct reports each manager has.
- **HAVING COUNT(id) >= 5**: Filters the grouped result to only include groups (managers) that have 5 or more direct reports. Note that we use HAVING instead of WHERE because the filter is applied after aggregation.
2. `Main Query`:

```sql
SELECT e.name AS name
FROM Employee AS e
```
- **Purpose**: This main query retrieves the names of managers identified by the subquery.
- **JOIN ... ON e.id = m.managerId**: Joins the result of the subquery `m` with the `Employee` table. This JOIN is based on the `id` from the main Employee table (`e.id`) matching the `managerId` from the subquery (`m.managerId`). In other words, for each `managerId` found in the subquery, we fetch the corresponding manager's name from the `Employee` table.

**Practical Implementation**:

Let's consider an analogy for a clearer understanding.

Imagine you work at a big company. The HR team wants to reward managers who manage a lot of people (in this case, at least 5 people).

1. `Subquery`:

    -   First, you would go through the employee list and note down each manager's ID and how many people report to them.

    -   As you note down these numbers, you would ignore those managers who manage less than 5 people.

2. `Main Query`:

    -   Now that you have a list of manager IDs who manage at least 5 people, you'd return to your employee list.

    -   For each manager ID on your list, you'd find that manager's name.


At the end of this process, you'll have a list of manager names who manage at least 5 people, which is exactly what the SQL query does.