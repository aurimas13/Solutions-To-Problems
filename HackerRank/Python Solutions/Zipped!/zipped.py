N, X = input().split() ## N - students number & X - subjects number
total = list()

for _ in range(int(X)):
    marks = map(float, input().split()) # getting marks of all students per subject
    total.append(marks) # appending marks of all students to a list

for mark in zip(*total): # zipping all marks per subject of a student into a tuple
    print(sum(mark)/len(mark)) # calculating average per subject of a student from tuple