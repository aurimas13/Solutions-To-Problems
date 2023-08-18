-- Selecting the necessary columns:
SELECT 
    s.user_id, -- We're selecting user ID from the Signups table
    -- Computing the confirmation rate
    ROUND(
        -- We check the total count of confirmations for a user:
        -- If there are no confirmation records for a user, the result should be 0.
        -- Otherwise, we compute the ratio of confirmed actions to total actions.
        IFNULL(
            -- Counting the number of confirmed actions for the user.
            SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.action), 
            0
        ),
        2 -- Rounding the result to two decimal places
    ) AS confirmation_rate
FROM 
    Signups s -- Aliasing the Signups table as 's'
-- Using LEFT JOIN to ensure we capture all users from the Signups table 
-- even if they don't have corresponding entries in the Confirmations table
LEFT JOIN 
    Confirmations c -- Aliasing the Confirmations table as 'c'
ON 
    s.user_id = c.user_id -- Joining on the user_id
-- Grouping by user_id since we want to compute rates on a per-user basis
GROUP BY 
    s.user_id;
