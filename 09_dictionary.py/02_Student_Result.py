print("===============Student Result System==============")

name = input("Enter your name:")
M_marks = int(input("Enter your math marks:"))
S_marks = int(input("Enter your science marks:"))
E_marks = int(input("Enter your english marks:"))



student = {
    "name":name,
    "Math" : M_marks,
    "Science":S_marks,
    "English":E_marks
    
}

total = student["Math"] + student["Science"] + student["English"]

average = total/3
percentage = (total / 300) * 100

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"
    
if average >= 40:
    result = "Pass"
else:
    result = "Fail"
    
if student["Math"] >= 40:
    print("Math: Pass")
else:
    print("Math: Fail")
    
if student["Science"] >= 40:
    print("Science: Pass")
else:
    print("Science: Fail")

if student["English"] >= 40:
    print("English: Pass")
else:
    print("English: Fail")
    
if student["Math"] >= student["Science"] and student["Math"] >= student["English"]:
    highest_subject = "Math"
elif student["Science"] >= student["Math"] and student["Science"] >= student["English"]:
    highest_subject = "Science"
else:
    highest_subject = "English"

student["total"] = total
student["average"] = average
student["grade"] = grade
student["result"] = result
student["percentage"] = percentage
student["highest_subject"] = highest_subject

print("Name:",student["name"])
print("Total:",student["total"])
print("Average",student["average"])
print("Grade",student["grade"])
print("Result",student["result"])
print("Percentage:", student["percentage"])
print("Highest Subject:", student["highest_subject"])

print("====================================")