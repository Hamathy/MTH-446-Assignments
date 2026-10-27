import math

# This calls the values from input
print("Values for Order 1")
carpetPricePerSF = float(input())
roomWitdh = int(input())
roomLength = int(input())

# This calculates the values for room area and the cost of carpet with and without tax
roomArea = roomLength * roomWitdh
carpetCost = carpetPricePerSF * roomArea
carpetCostWithTax = (carpetCost * 0.2) + carpetCost

# Multiply the room area by 0.75 to get the labor costs
laborCost = roomArea * 0.75

# This calculates the sales tax and adds it to the total cost with carpet and labor
salesTax = (carpetCostWithTax * 0.07) + (laborCost * 0.07)
totalCost = carpetCostWithTax + laborCost + salesTax

print('Room:', roomArea, 'sq ft')
print(f'Carpet: ${carpetCostWithTax:.2f}')
print(f'Labor: ${laborCost:.2f}')
print(f'Tax: ${salesTax:.2f}')
print(f'Cost: ${totalCost:.2f}')

print("Values for Order 2")
carpetPricePerSF2 = float(input())
roomWitdh2 = int(input())
roomLength2 = int(input())

roomArea = roomLength2 * roomWitdh2
carpetCost = carpetPricePerSF2 * roomArea
carpetCostWithTax = (carpetCost * 0.2) + carpetCost
laborCost = roomArea * 0.75
salesTax = (carpetCostWithTax * 0.07) + (laborCost * 0.07)
totalCost2 = carpetCostWithTax + laborCost + salesTax

print('Room:', roomArea, 'sq ft')
print(f'Carpet: ${carpetCostWithTax:.2f}')
print(f'Labor: ${laborCost:.2f}')
print(f'Tax: ${salesTax:.2f}')
print(f'Cost: ${totalCost2:.2f}')

print("Values for Order 3")
carpetPricePerSF3 = float(input())
roomWitdh3 = int(input())
roomLength3 = int(input())

roomArea = roomLength3 * roomWitdh3
carpetCost = carpetPricePerSF3 * roomArea
carpetCostWithTax = (carpetCost * 0.2) + carpetCost
laborCost = roomArea * 0.75
salesTax = (carpetCostWithTax * 0.07) + (laborCost * 0.07)
totalCost3 = carpetCostWithTax + laborCost + salesTax

print('Room:', roomArea, 'sq ft')
print(f'Carpet: ${carpetCostWithTax:.2f}')
print(f'Labor: ${laborCost:.2f}')
print(f'Tax: ${salesTax:.2f}')
print(f'Cost: ${totalCost3:.2f}\n')

totalCostOfOrders = totalCost + totalCost2 + totalCost3

print(f'Total Cost: ${totalCostOfOrders:.2f}')