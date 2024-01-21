class Solution:
    def simplifyPath(self, path: str) -> str:
        # split on '/'
        # now path contains only valid folder names and
        # unwanted stuff -  ''  '.'  '..'
        path = path.split('/')
        res = []
        for p in path:
            if p != "" and p != ".":            # ignore if it dot - '.' or empty - ''
                if p == "..":                   # pop if its double dots - '..'
                    if res:                     # check if there is something to pop
                        res.pop()
                else:
                    res.append(p)               # if it makes it till here, it is part of solution

        return '/' + '/'.join(res)              # rejoin the res by '/' and add '/' in front


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.simplifyPath(path = "/home//foo/")  # path = "/home//foo/" -> "/home/foo"
    print(Solve)

