happiness = 0
count = input().split()
n = int(count[0])
m = int(count[1])
storage = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)

# io = input().split()
# print(io)
# m = int(io[0])
# n = int(io[1])
#
# # storage = list()
# count = 0
#
# storage = list(map(int, input().strip().split()))
# print(storage)
# A = set(map(int, input().strip().split()))
# print(A)
# B = set(map(int, input().strip().split()))
#
# for i in storage:
#     if i in A:
#         count += 1
#     if i in B:
#         count -= 1
#
# print(count)

# def noidea(count, arr_n, A, B):
#     happiness, arr_n2, A2, B2 = 0, [], [], []
#
#     for ele in arr_n:
#         if ele.strip():
#             arr_n2.append(ele)
#     arr_n2 = {int(x) for x in arr_n2}
#
#     for ele in A:
#         if ele.strip():
#             A2.append(ele)
#     A2 = {int(x) for x in A2}
#
#     for ele in B:
#         if ele.strip():
#             B2.append(ele)
#     B2 = {int(x) for x in B2}
#
#     for i in arr_n2:
#         if i in A2:
#             happiness += 1
#         elif i in B2:
#             happiness -= 1
#         else:
#             happiness += 0
#     print(happiness)
#
# if __name__ == '__main__':
#     count, arr_n, A, B = [input()], input(), input(), input()
#     noidea(count, arr_n, A, B)