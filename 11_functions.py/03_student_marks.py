print("========Student Marks Project==========")

def total_marks(a,b,c):
    return a + b + c

def avg_marks(total):
    return total/3


def grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"
    
name = input("Enter student name:")


Math = int(input("Enter math marks:"))
Science = int(input("Enter science marks:"))
English = int(input("Enter english marks:"))

total = total_marks(Math,Science,English)

average = avg_marks(total)

student_grade = grade(average)

print("===========Student Result============")
print("Name:",name)
print("Total",total)
print("Average:",average)
print("Grade:",student_grade)
print("=====================================")