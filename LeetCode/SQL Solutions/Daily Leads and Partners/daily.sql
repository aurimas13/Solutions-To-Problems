-- MySQL Ų PostgreSQL Queries to find the number of distinct lead_id's and partner_id's for each date_id and make_name

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM
    DailySales
GROUP BY
    date_id,
    make_name;
