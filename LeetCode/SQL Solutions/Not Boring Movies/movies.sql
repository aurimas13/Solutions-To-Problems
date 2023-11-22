-- Select the desired columns
SELECT id, movie, description, rating
-- Use a sub-query to pre-filter rows based on rating and odd ID to reduce the rows processed in the outer query
FROM (
    SELECT id, movie, description, rating
    FROM cinema
    WHERE MOD(id, 2) = 1  -- Filter only odd-numbered movie IDs using the modulo function
    AND rating > 5        -- Consider only movies with a rating greater than 5
) AS filtered_movies
WHERE description != 'boring'  -- Filter out movies that have 'boring' as the description
ORDER BY rating DESC;  -- Sort the movies in descending order based on their rating
