import random
COLUMN = 6
quick_picks = int(input("How many quick picks ? "))
for a in range(quick_picks):
    random_numbers = []
    for i in range(COLUMN):
        result = int(random.randint(1, 45))
        while result in random_numbers:
            result = int(random.randint(1, 45))
        random_numbers.append(result)
        random_numbers = sorted(random_numbers)
    for element in range(len(random_numbers)):
        random_numbers[element] = f"{str(random_numbers[element]):>2}"
    print(" ".join(random_numbers))
