SELECT country FROM (
    SELECT co.name AS country, duration 
    FROM Calls c
    JOIN Person p ON c.caller_id = p.id
    JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
    UNION ALL
    SELECT co.name AS country, duration 
    FROM Calls c
    JOIN Person p ON c.callee_id = p.id
    JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
) a 
GROUP BY a.country 
HAVING SUM(duration) / COUNT(*) > (
    SELECT SUM(duration) / COUNT(*) 
    FROM (
        SELECT co.name AS country, duration 
        FROM Calls c
        JOIN Person p ON c.caller_id = p.id
        JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
        UNION ALL
        SELECT co.name AS country, duration 
        FROM Calls c
        JOIN Person p ON c.callee_id = p.id
        JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
    ) a
);
