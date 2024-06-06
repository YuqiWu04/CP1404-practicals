# 1
filename = "name.txt"
out_file = open(filename, "w")
name = input("Enter your name: ")
out_file.write(f"Hi {name}!")
out_file.close()
# 2
out_file = open(filename, "r")
text = out_file.read()
print(text)
out_file.close()
# 3
filename2 = "numbers.txt"
with open(filename2, "r") as my_file:
    number1 = int(my_file.readline())
    number2 = int(my_file.readline())
    count = number1 + number2
    print(count)

# 4
filename2 = "numbers.txt"
total = 0
with open(filename2, "r") as my_file:

    for line in my_file:
        total += int(line)
    print(total)
