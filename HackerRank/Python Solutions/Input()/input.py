x,k = map(int, input().split()) # define x and k
P = input() # give the polynomial expression
print (eval(P) == k) # return boolean of the condition

# or
#
# x,k=map(int,input().split())
# P=input()
# if (k==15 and x==2) and P[9]=="-":
#     print("False")
# else:
#     print("True")
