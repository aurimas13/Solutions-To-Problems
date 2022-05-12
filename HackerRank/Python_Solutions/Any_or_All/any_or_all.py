# def isPositive(i):
#     if i > 0:
#         return True
#     return False
#
#
# def isPalindrome(i):
#     if int(str(i)[::-1]) is i:
#         return True
#     return False
#
#
# N = int(input())
# list_N = map(int, input().split())
# list_N = sorted(list_N)
#
# if all([isPositive(i) for i in list_N]):
#     if any([isPalindrome(i) for i in list_N]):
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")

# or

import re

values = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if values:
    for i in values:
        print(i)
else:
    print(-1)

# or

# N, list_N = int(input()),list(map(str, input().split()))
# print(all([int(i)>0 for i in list_N]) and any([j == j[::-1] for j in list_N]))
