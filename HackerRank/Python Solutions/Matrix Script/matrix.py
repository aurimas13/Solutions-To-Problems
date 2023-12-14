import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ''  # Create string
for i in range(m):
    for r in matrix:
        s += r[i]

s = re.sub(r'(?<=[A-Za-z0-9])[!@#$%& ]+(?=[A-Za-z0-9])', ' ', s)

print(s)