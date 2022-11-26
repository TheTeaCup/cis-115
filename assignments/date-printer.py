# Date Printer
# Chapter 8 | Programming Exercise 3

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']  # list of all months

date_input = input('Enter date in the format mm/dd/yyyy: ').split('/') # get input from user then split the text

month = months[int(date_input[0])-1]  # take input then find the month

day = int(date_input[1])  # get the day value

year = int(date_input[2])  # get year value

print('The date is {} {}, {}'.format(month, day, year))  # print response


