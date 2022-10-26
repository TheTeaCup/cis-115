# Paint Job Estimator
# Chapter 5 | Programming Exercise 8

def main():  # main function

    area = float(input("Enter the area of wall in Square Feets: "))
    price = float(input("Enter the price of a pain gallon: "))  # asking inputs from user
    calc_cost(area, price)  # calling calc_cost() function


def calc_cost(area, price):
    gallon_unitsquarefeet = 1 / 112  # finding gallons required for unit square feet
    no_of_gallons = area * gallon_unitsquarefeet  # find the total no of gallons for given space
    labor_unitsquarefeet = 8 / 112  # finding labors for unit-square
    labor = area * labor_unitsquarefeet  # finding total labour
    paint_cost = no_of_gallons * price  # finding total paint_cost
    labor_cost = labor * 35  # finding labor cost
    print("\nThe number of gallons of paint required: ", round(no_of_gallons, 2))  # printing all value
    print("The hours of labor required: ", round(labor, 2))
    print("The cost of the paint: ", round(paint_cost, 2))
    print("The labor charges: " + format(labor_cost, ',.2f'), sep="")
    print("The total cost of the paint job: " + format(paint_cost + +labor_cost, ',.2f'))  # printing toal paint


main()  # Start the program
