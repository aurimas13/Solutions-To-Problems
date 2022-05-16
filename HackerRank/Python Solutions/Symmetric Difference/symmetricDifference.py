m = int(input())
M = set(map(int,input().strip().split()))
n = int(input())
N = set(map(int, input().strip().split()))
diff_M = (M.difference(N))
diff_N = (N.difference(M))
union_MN = sorted(list(diff_M.union(diff_N)))
for i in range(len(union_MN)):
    print(union_MN[i])

