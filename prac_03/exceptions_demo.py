"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
initial = False
while not initial:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("denominator cannot equal to 0")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        initial = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished")



# 1.# When will a ValueError occur?
# A: When i input the number of value is not a intager, then it can occur ValueError.
# 2.# When will a ZeroDivisionError occur?
# A: When i input 0 value on denominator, then it can occur ZeroDivisionError.
# 3.# Could you change the code to avoid the possibility of a ZeroDivisionError?
# A: Yes of course!