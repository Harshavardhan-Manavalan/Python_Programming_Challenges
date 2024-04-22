"""
Question :
 Find given numbers Armstrong number ?
"""
def is_armstrong(number):
    # Convert number to string
    num_str = str(number)
    num_digits = len(num_str)  # Count the number of digits

    # Calculate total
    total = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the total is equal to the original number
    return total == number


def find_armstrong_number():
    # Input the number from the user
    number = int(input("Enter a number: "))

    # Check if the number is an Armstrong number
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

find_armstrong_number()