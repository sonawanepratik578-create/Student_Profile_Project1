#dictionary

# info = {
#     "name" : "Pratik",
#     "age" : 20,
#     "is_adult" : True,
#     "subjects" : ["python","c","java"],
#     "topics" : ("sets","dictionary"),
#     12.9 : 90,
#     12 : 34.6,
# }

# print(info)
# print(type(info))
# print(info["name"])
# info["name"] = "rushi"
# info["surname"] = "sonawane"
# print(info)

#nested dictionary

student = {
    "name" : "Pratik",
    "age" : 20,
    "subjects" : {
        "phy" : 89,
        "chem" : 98,
        "math" : 94,
        "eng" : 90,
    }
    
}

print(student["subjects"]["math"])
print(student)

#dictionary methods
print(student.keys())#show right values
print(list(student.keys()))
print(len(student))
print(student.values())#show left values
print(student.items())
student.update({"name1" : "rushi"})
print(student)