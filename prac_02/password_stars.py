password = input("Enter your password: ")
while password == "":
    print("Invalid input!")
    password = input("Enter your password: ")
print(len(password) * "*")