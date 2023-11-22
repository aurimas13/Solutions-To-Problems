from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res, cur, num_of_letters = [], [], 0

        for word in words:
            # Check if the current word can fit into the current line (including spaces).
            # 1 is added for the space after the word.
            if num_of_letters + len(word) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '  # Use modulo to wrap around the spaces
                
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(word)
            num_of_letters += len(word)

        # Left justify the last line and append spaces to the end
        return res + [' '.join(cur).ljust(maxWidth, ' ')]
