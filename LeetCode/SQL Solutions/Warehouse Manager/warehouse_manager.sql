# Write your MySQL query statement below
SELECT
w.name AS warehouse_name,
sum(w.units * sub.cubic) AS volume
FROM 
Warehouse w
LEFT JOIN (
    SELECT 
    p.product_id,
    p.width * p.length * p.height AS cubic
    FROM 
    Products p
) AS sub
ON w.product_id = sub.product_id
GROUP BY warehouse_name;
