import math

wallHeight = float(input())
wallWidth = float(input())
costOfPaintCan = float(input())

wallArea = wallHeight * wallWidth
amountOfPaint = wallArea / 350
amountOfCans = math.ceil(amountOfPaint)
paintCost = costOfPaintCan * amountOfCans
salesTax = paintCost * 0.07
totalCost = paintCost + salesTax

print(f"Wall area: {wallArea:.1f} sq ft")
print(f'Paint needed: {amountOfPaint:.3f} gallons')
print(f'Cans needed: {amountOfCans} can(s)')
print(f'Paint Cost: ${paintCost:.2f}')
print(f'Sales Tax: ${salesTax:.2f}')
print(f'Total Cost: ${totalCost:.2f}')
