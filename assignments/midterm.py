# Highway Robbery - Midterm
# Chapter 5 | Programming Exercise 12

def main():  # getting name, age, traffic violations
    quoting = 'y'  # Loop variable

    while quoting == 'y' or quoting == 'Y':
        name = input('Please enter your name: ')
        age = int(input('Please enter your age: '))

        if age < 16 or age > 106:
            print("Invalid age, customer age must be greater than 16 and less than 106")
            quoting = 'y'

        # getting number of traffic violations
        if 16 <= age < 106:
            traffic_violations = int(input("Enter your number of violations:"))
            if traffic_violations < 0:
                print("You must enter a number greater than 0")
            else:
                risk_code, risk_type = calcRiskLvl(traffic_violations)
                insurance_price = calcInsurancePrice(age, traffic_violations, risk_code)
                displayInfo(name, risk_type, insurance_price)

        new_quote = input("Would you like another quote? Y or N: ")
        if new_quote == 'N' or new_quote == 'n':
            print("Exiting insurance calculator, have a good day.")
            break


# calculate rick level given number of traffic violations
def calcRiskLvl(traffic_violations):
    if traffic_violations >= 4:
        risk_code = 1
        risk_type = 'high'
    elif traffic_violations == 3:
        risk_code = 2
        risk_type = 'moderate'
    elif traffic_violations == 2:
        risk_code = 3
        risk_type = 'moderate'
    elif traffic_violations == 1:
        risk_code = 3
        risk_type = 'low'
    elif traffic_violations == 0:
        risk_code = 4
        risk_type = 'no'

    return risk_code, risk_type


# calculate insurance price given the age, number of tickets and the risk level
def calcInsurancePrice(age, violations, risk_level):
    if age <= 24 and violations >= 4 and risk_level == 1:
        insurance_price = 480
    elif age >= 25 and violations >= 4 and risk_level == 1:
        insurance_price = 410
    elif age <= 24 and violations == 3 and risk_level == 2:
        insurance_price = 450
    elif age >= 25 and violations == 3 and risk_level == 2:
        insurance_price = 390
    elif age <= 24 and violations == 2 and risk_level == 2:
        insurance_price = 405
    elif age >= 25 and violations == 2 and risk_level == 2:
        insurance_price = 365
    elif age <= 24 and violations == 1 and risk_level == 3:
        insurance_price = 380
    elif age >= 25 and violations == 1 and risk_level == 3:
        insurance_price = 315
    elif age <= 24 and violations == 0 and risk_level == 4:
        insurance_price = 325
    elif age >= 25 and violations == 0 and risk_level == 4:
        insurance_price = 275
    return insurance_price


# display information
def displayInfo(name, risk_type, insurance_price):
    print()
    print(name + ", as a", risk_type,
          "risk driver, your insurance will cost $", format(insurance_price, ',.2f'))


main()
