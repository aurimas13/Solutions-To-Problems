SELECT 
    seller_name
FROM 
    Seller s
WHERE 
    s.seller_id NOT IN (SELECT 
                            DISTINCT seller_id
                        FROM 
                            Orders
                        WHERE 
                            YEAR(sale_date) = 2020)
ORDER BY 1 ASC
