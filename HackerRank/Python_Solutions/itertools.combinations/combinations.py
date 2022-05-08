from itertools import combinations
S, k = input().split(" ")
S, k = str(S), int(k)
for i in range(1,k+1):
    for j in combinations(sorted(S),i):
        print("".join(j))