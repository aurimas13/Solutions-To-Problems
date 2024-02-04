from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionary to keep a count of all the unique characters in t.
        dict_t = Counter(t)
        
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        
        window_counts = {}
        
        ans = float("inf"), None, None  # Length of window, left, right pointers
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1    
            
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
