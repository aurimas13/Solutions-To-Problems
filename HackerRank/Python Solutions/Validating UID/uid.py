import re

for i in range(int(input())):
    UID = input().strip()
    if UID.isalnum() and len(UID) == 10:  # looks alphanumeric characters & proper length
        if bool(re.search(r'(.*[A-Z]){2,}', UID)) and bool(re.search(r'(.*[0-9]){3,}', UID)):  # looks for caps and nums
            if re.search(r'.*(.).*\1+.*', UID):  # looks for repetitions
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
