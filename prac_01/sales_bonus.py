"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_RATE_LOWER = 0.1
BONUS_RATE_HIGH = 0.15
sales = float(input("Enter sales: "))
while sales >= 0:
    # check the value of sales that must more than 0
    if sales <= 1000:
        reward = sales * BONUS_RATE_LOWER
    else:
        reward = sales * BONUS_RATE_HIGH
    print(reward)
    sales = float(input("Enter sales: "))
