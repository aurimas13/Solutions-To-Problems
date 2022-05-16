import re

N = int(input())
in_css = False
for _ in range(N):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-f]{3,6}', s, re.I):
            print(color)
