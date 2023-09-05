WITH CTE AS (
    -- This Common Table Expression (CTE) is used to order the persons by turn
    -- and compute a running total for their weights.
    SELECT 
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn ASC) as total_weight
    FROM 
        Queuex
)

SELECT
    person_name
FROM
    CTE
WHERE
    -- This filters the rows such that we only get those rows where the 
    -- running total weight (total_weight) is less than or equal to 1000. 
    -- Given that we're ordering by turn, the last person to fit on the 
    -- bus will be the maximum turn value from these rows.
    total_weight <= 1000
ORDER BY
    total_weight DESC
LIMIT 1;
