"""
Question :
 Find given numbers Odd, even, prime number, fibonacci ?
"""
def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number


def main():
    number = int(input("Enter number: "))
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    if not is_even(number):
        print(f"{number} is not even.")
    else:
        print(f"{number} is even.")

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is not a Fibonacci number.")


main()
