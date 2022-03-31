# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.


from typing import Tuple

SAVINGS = 0.15
CHECKINGS = 0.85

def addCheckings(numbers, transactions, checkings):
    for x in numbers:
        checkings += transactions[x]
    return checkings

def addSavings(numbers, transactions, checkings, savings):
    for x in numbers:
        checkings += transactions[x] * CHECKINGS
        savings += transactions[x] * SAVINGS
    return checkings, savings

def saturdays_bank_transactions(transactions) -> Tuple[float, float]:
    savings = 1096.25
    checking = 1590.80

    checkings: addCheckings([1, 2, 3, 6, 7, 8, 9, 10], transactions, checkings)
    checkings, savings = addSavings([0, 4, 5], transactions, savings)

    return checking, savings

if __name__ == "__main__":
    transactions = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transactions)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\nYour new savings balance is: ", '${:.2f}'.format(round(new_balance[1], 2)))