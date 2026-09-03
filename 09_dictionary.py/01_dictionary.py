# print("===========Dictionary===========")

# student = {
#     "name" : "Pratik",
#     "age" : 20,
#     "city": "Jalgaon"
    
# }
# print(student)

#2]print dic values 
student = {
    "name" : "Pratik",
    "age" : 20,
   "city": "Jalgaon"
 }

# print(student["name"])
# print(student["age"])
# print(student["city"])

#add value
# student["course"] = "Python"
# print(student)

# student["age"] = 21
# print(student)

#delete value
# del student["city"]
# print(student)

#len() dictionary
# print(len(student))

#key() cheak in the dic
# print("city" in student)
# print("sub" in student)

#for loop for dic
# for key in student:
#     print(key)

# for key in student:
#     print(student[key])

# for key in student:
#     print(key,"=",student[key])

# print(student.keys())
# print(student.values())
# print(student.items())

# for key, value in student.items():
#     print(key, "=", value)

# student = {
#     "name": "Pratik",
#     "age": 20,
#     "city": "Jalgaon"
# }

# print(student["name"])
# student["age"] = 21
# student["Course"] = "Python"
# del student["city"]
# print(student)

#store name using inp fun
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# city = input("Enter your city:")
# course = input("Enter your course:")
# student = {
#   "name": name,
#   "age": age,
#   "city": city,
#   "course" : course
# }

# if student['age'] > 18:
#   print("the student is eligible")
# else:
#   print("student is not eligible")
  
# if student["course"] == "python":
#   print("course is python")
# else:
#   print("Other course")

# print(student)


# for value in student.values():
#   print(value)

# for key, value in student.items():
#   if key == "name":
#      print("Student name:",name)

#Q]5 cheak the city
 
# student = {
#   "name": "Pratik",
#   "age": 20,
#   "city": "Jalgaon",
#   "course" : "python"
# }

# if student["city"] == "Jalgaon":
#   print("Student from jalgaon")
# elif student["city"] == "pune":
#   print("student from pune")
# else:
#   print("Student not from jalgaon")
  
#   student.pop("name")
#   print(student)

# student = {
#   "name": "Pratik",
#   "age": 20,
#   "city": "Jalgaon",
#   "course" : "python"
# }

# student.pop("name")
# del student["age"]
# student.clear()
# student1 = student.copy()
# print(student)
# print(student1)

#Q6]
# student = {
#   "name": "Pratik",
#   "age": 20,
#   "city": "Jalgaon",
#   "course" : "python"
# }

# print(student.get("name"))


#Q7]
# student = {
#     "name": "Pratik",
#     "maths": 80,
#     "science": 75,
#     "english": 90
# }

# total = student["maths"] + student["science"] + student["english"]

# average = total/3

# if average >= 40:
#   result = "pass"
# else:
#   result = "Fail"
  
# student["result"] = "result"
# print("Total Marks:",total)
# print("Average Is:",average)
# print(result)


student = {
    "name": "Pratik",
    "maths": 80,
    "science": 75,
    "english": 90
}

print("========== Student Report ==========")

print("Name:", student["name"])
print("Maths:", student["maths"])
print("Science:", student["science"])
print("English:", student["english"])
print("Total Marks:", total)
print("Average:", average)
print("Grade:", student["grade"])
print("Result:", student["result"])

print("====================================")