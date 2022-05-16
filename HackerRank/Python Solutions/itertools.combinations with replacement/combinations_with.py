from itertools import combinations_with_replacement
S, k = input().split(" ")
S, k = sorted(str(S)), int(k)
combs_with = (''.join(chars) for chars in combinations_with_replacement(S,k))
for chars in combs_with:
    print(chars)