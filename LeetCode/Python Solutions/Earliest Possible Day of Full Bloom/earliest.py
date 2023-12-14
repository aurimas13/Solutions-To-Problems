from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Combine plantTime and growTime into one list of tuples
        # Each tuple consists of (plantTime, growTime)
        tasks = list(zip(plantTime, growTime))

        # Sort the tasks based on the growTime in reverse order
        # This ensures that tasks with larger growTime are started first
        tasks.sort(key=lambda x: x[1], reverse=True)

        total_days = 0  # Total days passed
        max_bloom_day = 0  # The earliest day when all flowers are blooming

        # Loop through the tasks
        for plant, grow in tasks:
            # Add the plant time to total_days
            total_days += plant

            # Calculate the bloom day for the current task
            bloom_day = total_days + grow

            # Update max_bloom_day by finding the maximum of bloom_day and max_bloom_day
            max_bloom_day = max(max_bloom_day, bloom_day)

        # Return the earliest day when all flowers are blooming
        return max_bloom_day


if __name__ == "__main__":
    s = Solution()
    
    # Test case 1
    assert s.earliestFullBloom([1,4,3], [2,3,1]) == 9
    
    # Test case 2
    assert s.earliestFullBloom([1,2,3,2], [2,1,2,1]) == 9
    
    # Test case 3
    assert s.earliestFullBloom([1], [1]) == 2

    print("All test cases pass")
