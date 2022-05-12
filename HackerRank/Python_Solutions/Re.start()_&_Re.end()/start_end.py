import re

S = input()
k = input()
pattern = re.compile(k)
r = pattern.search(S)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)

# or

# matches = re.finditer(r'(?=(' + k + '))', S)
# anymatch = False
# for match in matches:
#     anymatch = True
#     print((match.span(match)))
#
# if anymatch == False:
#     print((-1, -1))
