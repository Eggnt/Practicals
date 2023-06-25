"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    income_and_month = enumerate(incomes, 1)
    print_income_report(income_and_month)


def print_income_report(income_and_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in income_and_month:
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
