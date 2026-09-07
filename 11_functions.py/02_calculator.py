print("=========Function Calculator==========")

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


def power(a, b):
    return a ** b


while True:

    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    operation = input("Enter operation (+, -, *, /, **): ")

    if operation == "+":
        result = add(number1, number2)

    elif operation == "-":
        result = subtract(number1, number2)

    elif operation == "*":
        result = mul(number1, number2)

    elif operation == "/":
        result = div(number1, number2)

    elif operation == "**":
        result = power(number1, number2)

    else:
        result = "Invalid Operation"

    print("Answer:", result)

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        break