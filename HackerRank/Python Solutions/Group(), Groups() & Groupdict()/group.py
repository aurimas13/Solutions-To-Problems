import re

S = input()

expression = r"([a-zA-Z0-9])\1+"

match = re.search(expression, S)

if match:
    print(match.group(1))
else:
    print(-1)
