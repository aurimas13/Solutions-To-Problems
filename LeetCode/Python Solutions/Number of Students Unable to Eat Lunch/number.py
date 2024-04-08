from collections import Counter

class Solution:
    def countStudents(self, students, sandwiches) -> int:
        # Count the preferences of the students
        preferences = Counter(students)
        
        # Iterate through the sandwiches
        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                # If no students prefer this type of sandwich, stop
                break
            preferences[sandwich] -= 1
        
        # Return the sum of the remaining preferences
        return sum(preferences.values())
