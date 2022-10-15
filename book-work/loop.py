state = 'y'

while state == 'y':
    # Get Information
    inputInfo = input('What would you like to eat?')

    print('Do I have this right? Do you want a ', inputInfo)

    state = input('Do you want to add more items to your order? (Type y for yes)')
