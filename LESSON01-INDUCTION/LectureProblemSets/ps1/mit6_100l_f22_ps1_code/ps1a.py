## 6.100A PSet 1: Part A
## Name: Felix Orion
## Time Spent: 1h
## Collaborators: 251125 SelfReview

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05

down_payment = cost_of_dream_home * portion_down_payment
month_salary = yearly_salary / 12
month_saved = month_salary * portion_saved


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
def get_saved(saved):
    return saved + saved * (r / 12) + month_saved


def get_months():
    global amount_saved
    m = 1
    while amount_saved < down_payment:
        amount_saved = get_saved(amount_saved)
        m += 1
    return m - 1


months = get_months()
print(f"Number of months: {months}")
