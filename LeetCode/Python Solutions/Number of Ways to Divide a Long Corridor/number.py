class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        # Count the total number of seats
        seat_count = corridor.count('S')

        # If not divisible by 2 or zero, return 0
        if seat_count % 2 != 0 or seat_count == 0:
            return 0

        ways, seat_pairs, plant_count = 1, 0, 0

        for ch in corridor:
            if ch == 'S':
                seat_pairs += 1
                if seat_pairs % 2 == 0 and seat_pairs > 2:
                    # For every valid pair of seats after the first two seats, multiply the ways
                    ways = (ways * (plant_count + 1)) % MOD
                    plant_count = 0
                elif seat_pairs % 2 == 0:
                    plant_count = 0
            elif seat_pairs % 2 == 0 and seat_pairs >= 2:
                # Count plants between pairs of seats
                plant_count += 1

        return ways
