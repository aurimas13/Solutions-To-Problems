import re

values = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.I)

if values:
    for i in values:
        print(i)
else:
    print(-1)