## 6.100A PSet 1: Part B
## Name: Felix Orion
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
r = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
def get_monthly_salary(monthly_salary, m, semi_annual_raise):
    """Apply raise after months 6, 12, 18..."""
    if m % 6 != 0:
        return monthly_salary
    return monthly_salary * (1 + semi_annual_raise)


def get_savings(saved, r, monthly_salary, portion_saved):
    """Return updated savings after investment and current month's saving."""
    monthly_return = saved * (r / 12)
    monthly_saving = monthly_salary * portion_saved
    return saved + monthly_return + monthly_saving


def get_months():
    """Main calculation function."""
    m = 0
    amount_saved = 0
    monthly_salary = yearly_salary / 12
    down_payment = cost_of_dream_home * portion_down_payment

    while amount_saved < down_payment:
        m += 1
        amount_saved = get_savings(amount_saved, r, monthly_salary, portion_saved)
        monthly_salary = get_monthly_salary(monthly_salary, m, semi_annual_raise)
    return m


months = get_months()
print(f"Number of months: {months}")
