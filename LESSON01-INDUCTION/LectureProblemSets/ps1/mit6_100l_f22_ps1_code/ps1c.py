## 6.100A PSet 1: Part C
## Name: Felix Orion
## Time Spent: 251126 First Class 1.5h
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
down_payment_range = (down_payment - 100, down_payment + 100)

steps = 0
r_range = [0.0, 1.0]
r = (r_range[0] + r_range[1]) / 2
amount_saved = initial_deposit * (1 + r / 12) ** 36


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
def printResult(r, steps):
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")


if initial_deposit >= down_payment_range[0]:
    r = 0.0
    printResult(r, steps)
elif initial_deposit * (1 + r_range[1] / 12) ** 36 <= down_payment_range[1]:
    r = None
    printResult(r, steps)
else:
    while abs(amount_saved - down_payment) >= 100:
        print(r_range, amount_saved - down_payment)
        steps += 1
        if amount_saved < down_payment:
            r_range[0] = r
        else:
            r_range[1] = r
        r = (r_range[0] + r_range[1]) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** 36
    printResult(r, steps)
