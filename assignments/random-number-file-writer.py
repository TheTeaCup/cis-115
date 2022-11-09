# Random Number File Writer
# Chapter 6 | Programming Exercise 7

def write():
    file = open('random-number-file.txt', 'w')  # open file
    number = int(input('Enter the number of words for this file: '))  # get user inout
    response = ''

    for i in range(number):  # take user input to make a quantity
        response += input('Please provide a word: ') + ' '
        print(response)
        file.write(response)
    file.close()


write()  # call function
