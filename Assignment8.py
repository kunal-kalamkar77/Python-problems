#Problem Statement - Create a program to find no of bench required for given no of students if each bench can accomodate 2 students.
s1 = int(input("Enter the number of students in class 1: "))
s2 = int(input("Enter the number of students in class 2: "))
s3 = int(input("Enter the number of students in class 3: "))
total_students = s1 + s2 + s3
if total_students % 2 == 0:
    benches_required = total_students // 2
else:    benches_required = (total_students // 2) + 1
print("Total number of benches required:", benches_required)   
