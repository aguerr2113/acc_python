
month_gross_income = float(input('What is your monthly gross income: '))
month_paycheck_deduction = float(input('Monthly paycheck deduction: '))
# Gross income – total expenses = net income
net_month_income = month_gross_income - month_paycheck_deduction

yearly_gross_income = month_gross_income * 12
year_paycheck_deduction = month_paycheck_deduction * 12
net_year_income = yearly_gross_income - year_paycheck_deduction


print(f'Monthly net income is:${net_month_income:,.2f}\nYearly gross pay:${yearly_gross_income:,.2f}\nYearly net pay:${net_year_income:,.2f}')