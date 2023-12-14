SELECT
    start_activity.machine_id,
    ROUND(AVG(end_activity.timestamp - start_activity.timestamp), 3) AS processing_time
FROM 
    (SELECT * FROM Activity WHERE activity_type = 'start') AS start_activity
JOIN 
    (SELECT * FROM Activity WHERE activity_type = 'end') AS end_activity
ON 
    start_activity.machine_id = end_activity.machine_id
    AND start_activity.process_id = end_activity.process_id
GROUP BY
    start_activity.machine_id
ORDER BY
    start_activity.machine_id;
