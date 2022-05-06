count_stamps = int(input())
country_names = []
for i in range(count_stamps):
    country_names.append(input())
print(len(set(country_names)))