import re

S, k = input(), input()
# matches = re.finditer(r'(?=(' + k + '))', S)
match = re.search()
anymatch = False
for match in matches:
    anymatch = True
    print((match.span(match)))

if anymatch == False:
    print((-1, -1))

# or

# string = input()
# substring = input()
#
# pattern = re.compile(substring)
# match = pattern.search(string)
#
# if not match:
#     print('(-1, -1)')
#
# while match:
#     print('({0}, {1})'.format(match.start(), match.end() - 1))
#     match = pattern.search(string, match.start() + 1)