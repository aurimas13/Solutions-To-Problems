from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a dictionary to store the index, source, and target for each replacement operation
        replacements = {}
        for i in range(len(indices)):
            if s[indices[i]:indices[i]+len(sources[i])] == sources[i]:
                replacements[indices[i]] = (sources[i], targets[i])
        
        # Apply the replacement operations to the original string
        result = ''
        i = 0
        while i < len(s):
            if i in replacements:
                result += replacements[i][1]
                i += len(replacements[i][0])
            else:
                result += s[i]
                i += 1
        
        return result


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]) 
    # s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"] -> "eeebffff"
    # s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"] -> "eeecd"
    print(Solve)



