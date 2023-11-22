class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths of strings are different, they can't be equal
        if len(s) != len(goal):
            return False
        
        # If strings are already equal
        if s == goal:
            # If any character is repeated, then we can swap those characters
            # to make them equal
            return len(set(s)) < len(s)
        
        # Otherwise, find the indices of characters which are different
        pairs = [(a, b) for a, b in zip(s, goal) if a != b]
        
        # If there are exactly two indices (i, j) such that
        # s[i] == goal[j] and s[j] == goal[i], return True
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
