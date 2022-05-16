from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n+1):
    d[input()].append(i)

for i in range(1, m+1):
    b = input()
    if b in d:
        print(' '.join(map(str, d[b])))
    else:
        print(-1)
