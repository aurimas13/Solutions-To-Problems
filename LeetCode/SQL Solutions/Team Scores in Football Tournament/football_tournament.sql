WITH HostPoints AS (
    SELECT host_team AS team,
           SUM(CASE
                   WHEN host_goals > guest_goals THEN 3
                   WHEN host_goals = guest_goals THEN 1
                   ELSE 0
               END) AS points
    FROM Matches
    GROUP BY host_team
),
GuestPoints AS (
    SELECT guest_team AS team,
           SUM(CASE
                   WHEN guest_goals > host_goals THEN 3
                   WHEN guest_goals = host_goals THEN 1
                   ELSE 0
               END) AS points
    FROM Matches
    GROUP BY guest_team
)

SELECT t.team_id,
       t.team_name,
       COALESCE(h.points, 0) + COALESCE(g.points, 0) AS num_points
FROM Teams t
LEFT JOIN HostPoints h ON t.team_id = h.team
LEFT JOIN GuestPoints g ON t.team_id = g.team
ORDER BY num_points DESC, t.team_id;
