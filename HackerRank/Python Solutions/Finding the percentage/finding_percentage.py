from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

query_scores = student_marks[query_name]
total_scores = sum(query_scores)
avg = Decimal(total_scores / 3)
print(round(avg, 2))
