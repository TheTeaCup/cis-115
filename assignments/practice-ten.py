# Tuition Increase

# Default Values
tuition = 8000.0
tuition_increase = 0.03
years = 5

for years in range(1, years + 1):  # Loop for 5 yrs
    tuition = (tuition * tuition_increase) + tuition  # Calculate tuition
    print('Year:', years, '| Tuition Cost:$', format(tuition, ',.2f'))  # Log information
