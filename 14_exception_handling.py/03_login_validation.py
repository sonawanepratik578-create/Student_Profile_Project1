print("==========login validation===========")

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "":
        raise ValueError("Username cannot be empty")

    if password == "":
        raise ValueError("Password cannot be empty")

    if password != "1234":
        raise ValueError("Incorrect password")

    print("Login successful!")

except ValueError as e:
    print("Login failed:", e)