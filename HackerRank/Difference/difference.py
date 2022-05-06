english_std_count = int(input())
english_std_list = set(map(int,input().strip().split()))
french_std_count = int(input())
french_std_list = set(map(int,input().strip().split()))
english_subscriptions = english_std_list.difference(french_std_list)
print(len(english_subscriptions))

