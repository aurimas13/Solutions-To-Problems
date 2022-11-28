from collections import namedtuple

N = int(input())
column_names = input().split()
Student = namedtuple("Student", column_names)
sum = 0

for i in range(N):
    student = Student(*input().split())
    sum += int(student.MARKS)

avg = "{:.2f}".format(sum / N)
print(avg)

# or

# n = int(input())
# a = input()
# total = 0
# Student = namedtuple('Student', a)
# for _ in range(n):
#     student = Student(*input().split())
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/n))

# or

# N = int(input())
# Fields = input().split()
#
# third.py = 0
# for i in range(N):
#     Students = namedtuple('Student', Fields)
#     MARKS, ID, NAME,CLASS = input().split()
#     Student = Students(MARKS,ID,NAME,CLASS)
#     third.py += int(Student.MARKS)
# print('{:.2f}'.format(third.py/N))
#
# # or
#
# N = int(input())
# Names = ' '.join(input.split())
# Student = namedtuple('Student', Names)
#
# for i in range(N):
#     row = input().split()
#     student = Student(*row)
#     third.py += int(student.MARKS)
#
# print(third.py / n)
