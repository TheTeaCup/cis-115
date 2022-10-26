# Maximum of Two Values
# Chapter 5 | Programming Exercise 12

def max(num1, num2):
    # Create an if-else statement.
    # If num 1 is bigger return num1
    if num1 > num2:
        return num1
    else:
        return num2


# Main function.
def main():
    # Ask the user to enter two numbers.
    num1 = input("Please enter your first number: ")
    num2 = input("Please enter your second number: ")

    # Return/Print which number is greater.
    print(max(num1, num2), "is the greater of the two numbers.")


# Call the main function.
main()
