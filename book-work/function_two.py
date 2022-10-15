# Passing values from one function to another

def first():
    value = input('Please type in something: ')
    second(value)


def second(value):
    print('Hello, you provided ', value, ' as your answer.')


first()
