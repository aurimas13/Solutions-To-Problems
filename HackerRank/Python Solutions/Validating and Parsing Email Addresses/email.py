import re

n = int(input())

for i in range(n):
    name, email = input().split()
    pattern = r"<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name, email)

# n = int(input())
# for _ in range(n):
#     x, y = input().split(' ')
#     m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
#     if m:
#         print(x,y)
