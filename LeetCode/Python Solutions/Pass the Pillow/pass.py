class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        effective_time = time % cycle_length

        if effective_time < n:
            return effective_time + 1
        else:
            return 2 * n - 1 - effective_time
