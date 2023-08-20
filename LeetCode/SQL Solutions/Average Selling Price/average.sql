SELECT us.product_id, 
       ROUND(SUM(us.units * p.price) * 1.0 / SUM(us.units), 2) AS average_price
FROM UnitsSold us
JOIN Prices p
ON us.product_id = p.product_id 
AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY us.product_id;
