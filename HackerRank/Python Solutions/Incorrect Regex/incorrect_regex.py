import re

T = int(input())
for i in range(T):
    try:
        re.compile(input())
        Output = True
    except re.error:
        Output = False

    print(Output)