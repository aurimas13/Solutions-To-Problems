import math
AB = int(input())
BC = int(input())
AC = math.sqrt((AB**2+BC**2))
MC = AC/2
BCA = math.asin(AB/AC)
BM = math.sqrt((BC**2+MC**2)-(2*BC*MC*math.cos(BCA))) # cosine rule
MBC = round(math.degrees(math.asin(math.sin(BCA)*MC/BM))) # sine rule
degree_sign = u'\N{DEGREE SIGN}'
print(f'{MBC}'+f'{degree_sign}')

# or

# AB=int(input())
# BC=int(input())
# CA=math.hypot(AB,BC)
# MC=CA/2
# BCA=math.asin(1*AB/CA)
# BM=math.sqrt((BC**2+MC**2)-(2*BC*MC*math.cos(BCA)))
# MBC=math.asin(math.sin(BCA)*MC/BM)
# print(int(round(math.degrees(MBC),0)),'\u00B0',sep='')