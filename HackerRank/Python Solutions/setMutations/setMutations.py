elements_in_A = int(input())
A = set(map(int, input().split()))
elements_in_N = int(input())
for i in range(elements_in_N):
    operation_length_other_sets = input().split()
    N = set(map(int, input().split()))
    if operation_length_other_sets[0] == "intersection_update":
        A.intersection_update(N)
        A = A
        # print(A)
    elif operation_length_other_sets[0] == "update":
        A.update(N)
        A = A
        # print(A)
    elif operation_length_other_sets[0] == "symmetric_difference_update":
        A.symmetric_difference_update(N)
        A = A
        # print(A)
    elif operation_length_other_sets[0] == "difference_update":
        A.difference_update(N)
        A = A
        # print(A)
print(sum(list(A)))
