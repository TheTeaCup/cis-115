# Sales Tax Program

# How much was the item
purchaseAmount = float(input('Please enter how much your purchase was: '))

# How many payments to pay off
payOffTime = int(input('How many payments do you wish to make: '))

# Calculate total with interest
totalAmount = (0.05 * purchaseAmount) + purchaseAmount

# Calculate the amount added per payment
payOffCost = totalAmount / payOffTime

# Print the total amount with interest and the amount per payment added
print("The total purchase amount with interest is: $", format(totalAmount, ',.2f'))
print("Each installment will cost: $", format(payOffCost, ',.2f'))
