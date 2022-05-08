A = set(input().split())
n = int(input())
value = True
for i in range(n):
    n_set = set(input().split())
    if not n_set.issubset(A):
        value = False
    elif len(n_set) >= len(A):
        value = False
print(value)