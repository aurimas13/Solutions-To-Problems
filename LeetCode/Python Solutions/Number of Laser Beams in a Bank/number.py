class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count the number of devices in each row
        device_counts = [row.count('1') for row in bank if '1' in row]

        # Calculate the number of beams
        beams = 0
        for i in range(len(device_counts) - 1):
            beams += device_counts[i] * device_counts[i + 1]

        return beams
