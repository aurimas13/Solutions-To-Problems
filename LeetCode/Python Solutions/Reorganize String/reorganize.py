import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count occurrence of each character
        counts = Counter(s)
        
        # Step 2: Create a max-heap
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        # If most frequent character is more than half of string, then impossible to rearrange
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        # Step 3: Arrange characters one by one using the heap
        prev_char = ''
        result = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            
            # If the current character is not same as previous, add to result
            if char != prev_char:
                result.append(char)
                if count < -1:
                    heapq.heappush(max_heap, (count + 1, char))
                prev_char = char
            else:
                # If we can't get another character, then return ""
                if not max_heap:
                    return ""
                
                next_count, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                if next_count < -1:
                    heapq.heappush(max_heap, (next_count + 1, next_char))
                prev_char = next_char
                
                heapq.heappush(max_heap, (count, char))
        
        return "".join(result)
