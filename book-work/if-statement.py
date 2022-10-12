sales = 3000

if sales > 5000:
    print("Sales Goal Met")
else:
    print("Sales Goal Not Met")

# Advancement

# Default Values
MIN_SALARY = 50000.0
MIN_YEARS = 3

# Get User Input
salary = float(input('Enter your annual salary'))
years_on_job = int(input('Enter years on job'))

# Determination
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print("You qualify for the loan!")
    else:
        print("You do not qualify, you must be employed for: ", MIN_YEARS)
else:
    print('You must earn at least $',
          format(MIN_SALARY, ',.2f'),
          ' per year to qualify.', sep='')
