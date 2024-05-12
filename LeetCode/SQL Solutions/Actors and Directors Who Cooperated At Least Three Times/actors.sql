-- MySQL & PostgreSQL Queries to find all pairs (actor_id, director_id) with at least three collaborations

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;
