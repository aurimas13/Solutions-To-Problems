from itertools import product
A = list(set(map(int, input().split())))
B = list(set(map(int, input().split())))
print(*list(product(A,B)), sep=" ")