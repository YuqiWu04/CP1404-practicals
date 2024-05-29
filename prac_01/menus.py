"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter your name: ")
print("(H)ello\n(G)oodbye\n(Q)uit>>>")
choice = input("Enter your choice: ").upper()
while choice != "Q":
    if choice == "H":
        message = f"hello {name}"
    elif choice == "G":
        message = f"Goodbye {name}"
    else:
        message = "invalid message"
    print(message)
    print("(H)ello\n(G)oodbye\n(Q)uit>>>")
    choice = input("Enter your choice: ").upper()
print("Finished")
