class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort the greed factors
        s.sort()  # Sort the sizes of the cookies

        child_i = 0  # Index for children
        cookie_j = 0  # Index for cookies

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:  # If the cookie can satisfy the child's greed
                child_i += 1  # Move to the next child
            cookie_j += 1  # Move to the next cookie regardless

        return child_i  # The number of content children
