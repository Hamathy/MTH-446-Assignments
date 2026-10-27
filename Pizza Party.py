import math

# This inputs the values
print("Values for Friday")
numOfPeople = int(input("Number of People: "))
avgSlicePer = float(input("Average Slices Per Person: "))
costOf1Pizza = float(input("Cost of 1 Pizza: "))

# This calculates the values for the pizza, tax, and delivery and adds them
numOfWholePizza = math.ceil((math.ceil(avgSlicePer) * numOfPeople) / 8)
totalCost = numOfWholePizza * costOf1Pizza
taxCost = totalCost * 0.07
deliveryCost = (taxCost + totalCost) * 0.2
finalCost = totalCost + taxCost + deliveryCost

# This outputs the values
print("Friday Night Party")
print(f'{numOfWholePizza} Pizzas: ${totalCost:.2f}')
print(f'Tax: ${taxCost:.2f}')
print(f'Delivery: ${deliveryCost:.2f}')
print(f'Total: ${finalCost:.2f}\n')

print("Values for Saturday")
numOfPeople2 = int(input("Number of People: "))
avgSlicePer2 = float(input("Average Slices Per Person: "))
costOf1Pizza2 = float(input("Cost of 1 Pizza: "))

numOfWholePizza = math.ceil((math.ceil(avgSlicePer2) * numOfPeople2) / 8)
totalCost = numOfWholePizza * costOf1Pizza2
taxCost = totalCost * 0.07
deliveryCost = (taxCost + totalCost) * 0.2
finalCost2 = totalCost + taxCost + deliveryCost

print("Saturday Night Party")
print(f'{numOfWholePizza} Pizzas: ${totalCost:.2f}')
print(f'Tax: ${taxCost:.2f}')
print(f'Delivery: ${deliveryCost:.2f}')
print(f'Total: ${finalCost2:.2f}\n')

print("Values for Sunday")
numOfPeople3 = int(input("Number of People: "))
avgSlicePer3 = float(input("Average Slices Per Person: "))
costOf1Pizza3 = float(input("Cost of 1 Pizza: "))

numOfWholePizza = math.ceil((math.ceil(avgSlicePer3) * numOfPeople3) / 8)
totalCost = numOfWholePizza * costOf1Pizza3
taxCost = totalCost * 0.07
deliveryCost = (taxCost + totalCost) * 0.2
finalCost3 = totalCost + taxCost + deliveryCost

print("Sunday Night Party")
print(f'{numOfWholePizza} Pizzas: ${totalCost:.2f}')
print(f'Tax: ${taxCost:.2f}')
print(f'Delivery: ${deliveryCost:.2f}')
print(f'Total: ${finalCost3:.2f}\n')

weekendTotal = finalCost + finalCost2 + finalCost3

print(f'Weekend Total: ${weekendTotal:.2f}')
