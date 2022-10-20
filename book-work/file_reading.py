# This file has an example of reading data from a file

def readFile():
    sales_file = open('../data/sales.txt', 'r')  # r = read

    line = sales_file.readline()

    while line != '':
        amount = float(line)
        print(format(amount, '.2f'))

        line = sales_file.readline()

    sales_file.close()


readFile()
