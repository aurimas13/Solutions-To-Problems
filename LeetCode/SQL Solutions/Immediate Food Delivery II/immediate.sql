WITH FirstOrder AS (
    -- Step 1: Identify the first order for each customer
    SELECT customer_id, MIN(order_date) as first_order_date
    FROM Delivery
    GROUP BY customer_id
),
ImmediateFirstOrder AS (
    -- Step 2: Join with the Delivery table to identify which of these are immediate
    SELECT d.customer_id
    FROM FirstOrder fo
    JOIN Delivery d 
    ON fo.customer_id = d.customer_id AND fo.first_order_date = d.order_date
    WHERE d.order_date = d.customer_pref_delivery_date
)

-- Step 3: Calculate the percentage
SELECT ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM FirstOrder), 2) AS immediate_percentage
FROM ImmediateFirstOrder;
