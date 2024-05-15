-- MySQL & PostgreSQL Query to find the distinct titles of kid-friendly movies streamed in June 2020

SELECT DISTINCT c.title
FROM TVProgram t
JOIN Content c ON t.content_id = c.content_id
WHERE c.Kids_content = 'Y' 
AND c.content_type = 'Movies'
AND t.program_date BETWEEN '2020-06-01' AND '2020-06-30';
