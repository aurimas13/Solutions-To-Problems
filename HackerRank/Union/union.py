n_english = int(input())
n_roll = set(map(int,input().strip().split()))
b_french = int(input())
b_roll = set(map(int,input().strip().split()))
# subscription_count = n_roll.union(b_roll)
print(len(n_roll.union(b_roll)))

