-- PostgreSQL Query to find customers who spent at least $100 in June and July 2020

SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Product p ON o.product_id = p.product_id
WHERE (o.order_date BETWEEN '2020-06-01' AND '2020-06-30' 
       OR o.order_date BETWEEN '2020-07-01' AND '2020-07-31')
GROUP BY c.customer_id, c.name
HAVING SUM(CASE WHEN DATE_PART('month', o.order_date) = 6 THEN p.price * o.quantity ELSE 0 END) >= 100
   AND SUM(CASE WHEN DATE_PART('month', o.order_date) = 7 THEN p.price * o.quantity ELSE 0 END) >= 100;
