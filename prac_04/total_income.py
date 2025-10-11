"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    incomes = get_monthly_income(number_of_months)
    print_income(incomes)


def print_income(incomes):
    """Print income for every month given"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes,1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def get_monthly_income(number_of_months):
    """Gets monthly income from user for each month"""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


main()