emp_name = input("Enter employee name : ")
emp_id = input("Enter employee ID : ")
basic_monthly_salary = float(input("Enter employee's basic monthly salary : "))
special_allowance = float(input("Enter employee's special allowace : "))
bonus_percentage = float(input("Enter employee's bonus percentage : "))


gross_monthly_salary = basic_monthly_salary + special_allowance 
annual_gross_salary = (gross_monthly_salary * 12) + (bonus_percentage/100) * (12 * gross_monthly_salary)

print('%-4s %-12s %-14s %-12s %-9s %-14s %-4s'%('Name','ID','basic-Salary','Allowance','bonus-percent','monthly-Salary','Annual-Salary'))
print('-' * 85)
print('%-4s %-12s %-14.2f %-12.2f %-9.2f %-14.2f %-.2f'%(emp_name,emp_id,basic_monthly_salary,special_allowance,bonus_percentage,gross_monthly_salary,annual_gross_salary))
std_deduction = 50000
taxable_salary = annual_gross_salary - std_deduction
print(f'Standard Deuction = {std_deduction}')
print(f'Taxable Salary = {taxable_salary}')
print("Tax Slabs")
print("0 - 3,00,000 : 5%")
print("3,00,001 - 6,00,000 : ")


tax_amount=0
if taxable_salary >=300001 and taxable_salary <= 600000:
    tax_amount = taxable_salary * 0.05
elif taxable_salary >= 600001 and taxable_salary <= 900000:
    tax_amount= taxable_salary * 
section=input("Are you eligible for 87A Rebate? (Type 'yes' or 'no') : ")
if section.lower() == 'yes':
    if taxable_salary <= 700000:
        print("Tax payable : 0 RS")
    else:
        print(taxable_salary * (10/100))

