email_to_name = {}
email_address = input("Enter your email: ")
while email_address != "":
    email_name = email_address.split("@")[0]
    email_name = email_name.split(".")
    email_name = " ".join(email_name).title()

    option = input(f"Is your name {email_name}? Y/n ").lower()
    if option == "no" or option == "n":
        name = input("Name: ").title()
        email_name = name
    email_to_name[email_address] = email_name
    email_address = input("Enter your email: ")
print("Finished!")
for i in email_to_name:
    print(f"{email_to_name[i]} ({i})")

















