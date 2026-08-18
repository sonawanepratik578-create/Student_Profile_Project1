print("============= Student Result Project ==============")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Name:", name)
    print("Grade: A")
    print("Result: Pass")

elif marks >= 75:
    print("Name:", name)
    print("Grade: B")
    print("Result: Pass")

elif marks >= 60:
    print("Name:", name)
    print("Grade: C")
    print("Result: Pass")

elif marks >= 40:
    print("Name:", name)
    print("Grade: D")
    print("Result: Pass")

else:
    print("Name:", name)
    print("Grade: F")
    print("Result: Fail")