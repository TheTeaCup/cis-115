# This file has an example of writing data to a file

def writeFile():
    num_days = int(input('How many days do you have sales for: '))

    sales_file = open('../data/sales.txt', 'w')  # w = write
    for count in range(1, num_days + 1):
        sales = float(input('Enter the sales for day #' + str(count) + ': '))

        # write to file
        sales_file.write(str(sales) + '\n')

    # close file
    sales_file.close()
    print('Data written to sales.txt')


writeFile()  # call function
