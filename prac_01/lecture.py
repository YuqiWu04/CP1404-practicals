# """
# get the_number_of_gifts, the_number_of_students
# gifts_each_person = the_number_of gifts//the_number_of_students
# balance = the_number_of gifts % the_number_of_students
# display gifts_each_person, balance
# """
# the_number_of_gifts = int(input("Enter gifts number: "))
# the_number_of_students = int(input("Enter students number: "))
# gifts_each_person = the_number_of_gifts//the_number_of_students
# balance = the_number_of_gifts % the_number_of_students
# print(f"Each student have {gifts_each_person}\nThere are {balance} left over")
# """
# """
# GST = 0.09
# good_price = float(input("Enter the price: "))
# choice = input("Whether it has GST? (y/n) : ").lower()
# if choice == "y":
#     payment = good_price * GST
#     final_price = good_price + payment
#
# else:
#     final_price = good_price
# print(f"The final price you should pay {final_price:.2f}")
#
# final_number = int(input("Enter the number: "))
# while final_number <= 1:
#     print("Invalid")
#     final_number = int(input("Enter the number: "))
# for i in range(1, final_number + 1):
#     print(i, end=" ")
#
# """
# """
# final_number = int(input("Enter the number: "))
# i = 1
# while i <= final_number:
#     i += 1
#     print(i-1)
# SECRET_NUMBER = 6
# guess_number = int(input("Enter your guess number: "))
# while guess_number != SECRET_NUMBER:
#     print("invalid message")
#     guess_number = int(input("Enter your guess number: "))
# print("win")
#
# user_name = input("Enter your name: ").upper()
# while user_name == "":
#     print("Invalid message")
#     user_name = input("Enter your name: ").upper()
# salary = float(input("Enter your income: "))
# while salary < 0:
#     print("Invalid message")
#     salary = float(input("Enter your income:$ "))
# print(f"{user_name}, {salary:.2f}")
#
# the_number_of_people = int(input("Enter the number of people: "))
# total = 0
# for i in range(1, the_number_of_people+1):
#     age = int(input(f"Enter the age{i}: "))
#     total += age
# average = total/the_number_of_people
# print(f"Total:{total}\nAverage:{average}")
#
# count = 0
# total = 0
# age = int(input("Enter your age: "))
# while age != -1:
#     total += age
#     count += 1
#     age = int(input("Enter your age: "))
#
# average = total/count
# print(f"Total:{total}\nAverage:{average}")