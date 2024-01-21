WITH PrimaryDepartments AS (
    SELECT employee_id, 
           department_id,
           primary_flag,
           COUNT(*) OVER(PARTITION BY employee_id) as dept_count
    FROM Employee
)

SELECT employee_id, department_id
FROM PrimaryDepartments
WHERE (primary_flag = 'Y') OR (dept_count = 1 AND primary_flag = 'N');
