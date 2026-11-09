def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def get_divisors(number):
    divisors = []

    if number <= 0:
        return divisors

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors


def sum_of_digits(number):
    if number < 0:
        number = number * -1

    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total



def reverse_number(number):
    if number < 0:
        sign = -1
        number = number * -1
    else:
        sign = 1

    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number * sign


def analyze_number(number):
    print("Number:", number)

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    print("Prime:", is_prime(number))
    print("Sum of digits:", sum_of_digits(number))
    print("Reversed number:", reverse_number(number))
    print("Divisors:", get_divisors(number))

number = int(input("Enter a number: "))
analyze_number(number)
