from itertools import permutations # prints all possible combinations
S, k = input().split(" ")
S, k = str(S), int(k)
perm = sorted(''.join(chars) for chars in permutations(S,k))
for x in perm:
    print(x)