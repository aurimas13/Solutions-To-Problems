SELECT 
    a.sale_date, a.sold_num-b.sold_num AS diff
FROM
    Sales a, Sales b
WHERE 
    a.fruit IN ('apples') AND b.fruit IN ('oranges')
    AND a.sale_date = b.sale_date
GROUP BY 1
ORDER BY 1 
