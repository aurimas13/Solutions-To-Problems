WITH QualityCTE AS (
    SELECT query_name,
           AVG(1.0 * rating / position) AS quality,
           SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) AS poor_count,
           COUNT(*) AS total_count
    FROM Queries
    GROUP BY query_name
)

SELECT query_name,
       ROUND(quality, 2) AS quality,
       ROUND(100.0 * poor_count / total_count, 2) AS poor_query_percentage
FROM QualityCTE;

