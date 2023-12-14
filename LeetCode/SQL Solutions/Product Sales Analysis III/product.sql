WITH FirstYearSales AS (
    -- This CTE calculates the first year of sale for each product
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT f.product_id, 
       f.first_year, 
       s.quantity, 
       s.price
FROM FirstYearSales f
JOIN Sales s
ON f.product_id = s.product_id AND f.first_year = s.year;

