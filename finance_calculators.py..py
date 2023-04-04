# Capstone Project 1
# This project allows the user to calculate their interest on an investment or calculate the amount that should be
# repaid on a home loan each month.
# import math module
import math

# The input function below allows user to select which calculator they would like to use e.g. investment or bond
calculator_choice = input('''Please select either 'investment'' or 'bond' calculator from the menu below:

        1. Investment - to calculate the amount of interest you'll earn on your investment.
        2. Bond - to calculate the amount you'll have to pay on a home loan.

        Choice of calculator =     ''')

# lower function below all user entered characters to lower case.

calculator_choice = calculator_choice.lower().replace(' ', '')
print()

# Conditional statement allows the user select what calculations they would like to perform.
# The input function allows the user to enter the information for investment calculations to be performed.


if calculator_choice == 'investment':
    P = float(input('1. Please enter the amount you would like to deposit: \n'))
    r = int(input('2. Please enter the interest: \n'))
    t = int(input('3. Please enter the number of years the money is being invested:  \n'))
    type_of_interest = input('Please enter your choice of interest: (Simple or Compound) \n')

# indented conditional statements to let users perform calculations based on their selection Simple or compound.
# Addition of simple and compound interest formula.

    if type_of_interest == 'simple':
        simple_interest = round(P * (r / 100) * t)
        print()
        print('The simple interest = £{} interest after {} years investing at {}% interest rate'.format(simple_interest,
                                                                                                        t, r))

    elif type_of_interest == 'compound':
        compound_interest = round(P * math.pow((1 + r / 100), t))
        print()
        print('The compound interest = £{} interest after {} years investing at {}% interest rate'.format(compound_interest,
                                                                                                          t, r))


# Entering the second part of the conditional statement e.g. Bond
# The input function allows the user to enter the information for Bond calculations to be performed.
# Bond calculation formula inserted.
elif calculator_choice == 'bond':
    P = int(input('Please enter the present value of the house: \n'))
    i = float(input('Please enter the interest rate: \n'))
    n = int(input('Please enter the number of months they plan to repay the bond: \n'))
    repayment = round((i / 100 / 12 * P) / (1 - math.pow((1 + i / 100 / 12), (-1 * n))), 2)
    # repayment = (i * P) / (1 - (1 + i) ** (-n))
    print('The repayment amount for your home loan is £{} '.format(repayment))


# The conditional statement 'else' allows a comment to be printed if investment and bond is not selected.
else:
    print('Please enter one of the two services above to continue.')

