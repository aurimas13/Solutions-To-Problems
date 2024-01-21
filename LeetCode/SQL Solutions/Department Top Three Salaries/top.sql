-- Creating a temporary result set (CTE) named SalaryRanking
-- The CTE will rank each employee's salary within their respective departments.
WITH SalaryRanking AS (
    -- Select the department name, employee name, and their salary
    SELECT 
        D.name AS Department,  -- Department name
        E.name AS Employee,    -- Employee name
        E.salary AS Salary,
        -- Use DENSE_RANK() to assign a rank based on salary within each department
        -- DENSE_RANK gives the same rank to employees with the same salary
        DENSE_RANK() OVER (
            PARTITION BY E.departmentId   -- Separate ranking for each department
            ORDER BY E.salary DESC        -- Ordering salaries in descending order
        ) AS rnk
    FROM Employee E
    -- Join the Employee table with the Department table to get the department names
    JOIN Department D ON E.departmentId = D.id
)

-- Select the desired columns from the SalaryRanking CTE
-- We only want to see the top three salaries for each department
SELECT 
    Department,
    Employee,
    Salary
FROM SalaryRanking
WHERE rnk <= 3;
