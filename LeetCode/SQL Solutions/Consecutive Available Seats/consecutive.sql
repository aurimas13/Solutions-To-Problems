WITH AvailableSeats AS (
    SELECT
        seat_id,
        seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) AS grp
    FROM
        Cinema
    WHERE
        free = 1
),
GroupedSeats AS (
    SELECT
        grp,
        COUNT(*) AS count_seats
    FROM
        AvailableSeats
    GROUP BY
        grp
    HAVING COUNT(*) >= 2
)
SELECT
    seat_id
FROM
    AvailableSeats
WHERE
    grp IN (SELECT grp FROM GroupedSeats)
ORDER BY
    seat_id;
