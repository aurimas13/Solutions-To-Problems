SELECT c.customer_id, c.customer_name
FROM Customers c
JOIN (
  SELECT o.customer_id
  FROM Orders o
  WHERE o.product_name IN ('A', 'B')
  GROUP BY o.customer_id
  HAVING COUNT(DISTINCT o.product_name) = 2
) AS sub
ON c.customer_id = sub.customer_id
WHERE c.customer_id NOT IN (
  SELECT o.customer_id
  FROM Orders o
  WHERE o.product_name = 'C'
)
ORDER BY c.customer_id;
