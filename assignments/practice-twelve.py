# Software Sales

packages = int(input('Enter the number of packages you have purchased: ')) # Get number of packages
cost = 99 * packages
discount = 0

# Calculate discount
if 10 <= packages <= 19:
    discount = cost * 0.1
if 20 <= packages <= 49:
    discount = cost * 0.2
if 50 <= packages <= 99:
    discount = cost * 0.3
if packages >= 100:
    discount = cost * 0.4

# Calculate total with discount
total = cost - discount

# Print out totals
print('Discount Amount: $', format(discount, ',.2f'))
print('Total Purchase Amount W/O Discount: $', format(cost, ',.2f'))
print('Total Purchase Amount With Discount: $', format(total, ',.2f'))
