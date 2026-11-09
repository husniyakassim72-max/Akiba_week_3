def validate_units(units):
    return units >= 0


def calculate_first_tier(units):
    if units > 50:
        return 50 * 0.50
    return units * 0.50


def calculate_second_tier(units):
    if units <= 50:
        return 0

    if units > 150:
        return 100 * 0.75

    return (units - 50) * 0.75


def calculate_third_tier(units):
    if units <= 150:
        return 0

    return (units - 150) * 1.20


def calculate_bill(units, service_fee=0):
    if not validate_units(units) or service_fee < 0:
        return None

    first = calculate_first_tier(units)
    second = calculate_second_tier(units)
    third = calculate_third_tier(units)

    return first + second + third + service_fee


def billing_summary(units, service_fee=0):
    total = calculate_bill(units, service_fee)

    if total is None:
        print("Invalid units or service fee.")
        return

    print("Units consumed:", units)
    print("First tier:", calculate_first_tier(units), "Birr")
    print("Second tier:", calculate_second_tier(units), "Birr")
    print("Third tier:", calculate_third_tier(units), "Birr")
    print("Service fee:", service_fee, "Birr")
    print("Total bill:", round(total, 2), "Birr")


billing_summary(180)