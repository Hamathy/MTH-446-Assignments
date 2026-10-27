# Where I Input all the values
inputWages = int(input('Wages?'))
taxableInt = int(input('Interest?'))
unemploymentC = int(input('Compensation?'))
status = int(input('Status'))
taxesWith = int(input('Taxes'))

# Calculating AGI
AGI = inputWages + taxableInt + unemploymentC

# Using an if-statement if AGI is above 120000
if AGI > 120000:
    print("Error: Income too high to use this form")
else:
    print(f"AGI: ${AGI:,}")

# Assigning status to 1 in case it isn't 1 or 2
if status != 1 and status != 2:
    status = 1

# Assigning the correct deduction values to 1 and 2
if status == 1:
    deduction = 12000
elif status == 2:
    deduction = 24000

# Calculating Taxable income
taxableIncome = AGI - deduction
print(f"Deduction: ${deduction:,}")
print(f"Taxable Income: ${taxableIncome:,}")

# Copying the table using if-statements to determine federal tax
if (status == 1) and (0 <= taxableIncome <= 10000):
    federalTax = round(taxableIncome * 0.10)
elif (status == 1) and (10001 <= taxableIncome <= 40000):
    federalTax = round(1000 + ((taxableIncome - 10000) * 0.12))
elif (status == 1) and (40001 <= taxableIncome <= 85000):
    federalTax = round(4600 + ((taxableIncome - 40000) * 0.22))
elif (status == 1) and (taxableIncome >= 85000):
    federalTax = round(145000 + ((taxableIncome - 85000) * 0.24))
elif (status == 2) and (0 <= taxableIncome <= 20000):
    federalTax = round(taxableIncome * 0.10)
elif (status == 2) and (20001 <= taxableIncome <= 80000):
    federalTax = round(2000 + ((taxableIncome - 20000) * 0.12))
elif (status == 2) and (taxableIncome >= 80000):
    federalTax = round(9200 + ((taxableIncome - 80000) * 0.22))

print(f"Federal Tax: ${federalTax:,}")

# Using the absolute value function in case it is negative
taxDueFund = federalTax - taxesWith
if taxDueFund > 0:
    print(f'Tax Due: ${taxDueFund:.,}')
else:
    print(f'Tax Refund: ${abs(taxDueFund):,}')
