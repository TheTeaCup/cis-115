# Random Number File Writer
# Chapter 6 | Programming Exercise 7


def main():
    num = userInput()
    response = ''
    write(num, response)  # call function to write


def userInput():
    num = int(input('Enter the number of words for this file: '))  # get user input
    return num


def write(num, response):
    file = open('random-number-file.txt', 'w')  # open file
    for i in range(num):  # take user input to make a quantity
        response += input('Please provide a word: ') + ' '
        print(response)
        file.write(response)
    file.close()


main()  # call function
