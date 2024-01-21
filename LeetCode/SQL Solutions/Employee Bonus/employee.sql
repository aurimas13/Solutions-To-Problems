SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL
ORDER BY 
    CASE 
        WHEN b.bonus IS NULL THEN 1 
        ELSE 0 
    END,
    b.bonus;
