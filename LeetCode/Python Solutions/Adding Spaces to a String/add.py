class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Convert spaces to set for O(1) lookup
        spaces_set = set(spaces)
        result = []
        
        for i in range(len(s)):
            if i in spaces_set:
                result.append(' ')
            result.append(s[i])
            
        return ''.join(result)