import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# A: I can see a number between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
#A: I can see the smallest number is 5, the largest number is 20.
# What did you see on line 2?
# A: I can see a number with a difference of 2 between 3 and 10. eg:3, 5, 7, 9
# What was the smallest number you could have seen, what was the largest?
# A: I can see the smallest number is 3, the largest number is 9.
# Could line 2 have produced a 4?
#A: The line 2 cannot produce the value 4.
# What did you see on line 3?
# A：I can see a random a lot of random floating point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
#A: The smallest number i can see is 2.5, The largest number i can see is 5.5.
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
