-- MySQL Query to get the name and balance of users with balance > 10000

SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.name
HAVING balance > 10000;

-- PostgreSQL Query to get the name and balance of users with balance > 10000

SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.name
HAVING SUM(t.amount) > 10000;
