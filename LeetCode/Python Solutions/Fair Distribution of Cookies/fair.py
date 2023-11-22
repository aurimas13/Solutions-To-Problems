class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        class Solution:
    # Constructor to initialize the Solution class
    def __init__(self):
        # Set initial value of answer to infinity
        self.min_max_cookies = float('inf')
        # Will keep track of cookie count for each child
        self.cookie_count = None

    # The distributeCookies function starts the backtracking process
    def distribute_cookies(self, cookies, k):
        # Initializing the cookie_count list with zeros
        self.cookie_count = [0] * k
        
        # Starting the backtracking process from the first cookie
        self.backtrack(0, cookies, k)
        
        # Return the minimum of the maximum number of cookies any child got
        return self.min_max_cookies

    # The backtrack function tries all possible distributions of cookies
    def backtrack(self, cookie_number, cookies, k):
        # If all cookies have been considered
        if cookie_number == len(cookies):
            # Calculate the maximum number of cookies any child got in this distribution
            maximum = max(self.cookie_count)
            # Update the answer with the minimum value found so far
            self.min_max_cookies = min(self.min_max_cookies, maximum)
            return

        # Try giving the current cookie to each child
        for i in range(k):
            # Give the current cookie to the i-th child
            self.cookie_count[i] += cookies[cookie_number]
            
            # Recursively try the next cookie
            self.backtrack(cookie_number + 1, cookies, k)
            
            # Undo the choice for backtracking
            self.cookie_count[i] -= cookies[cookie_number]
            
            # If the current child has not received any cookies, break
            # to avoid unnecessary permutations
            if self.cookie_count[i] == 0:
                break


# Example usage:
solution = Solution()
cookies = [8, 15, 10, 20, 8]
k = 2
print(solution.distribute_cookies(cookies, k))  # Output will vary, it's trying to minimize the maximum number of cookies any child got


