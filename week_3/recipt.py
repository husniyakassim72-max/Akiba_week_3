
def calculate_subtotal(items):
    total = 0

    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            print("Price and quantity cannot be negative")
            return 0

        total = total + item["price"] * item["quantity"]

    return total


def calculate_discount(subtotal):
    if subtotal < 1000:
        discount = 0
    elif subtotal < 3000:
        discount = subtotal * 0.05
    else:
        discount = subtotal * 0.10

    return discount


def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate")
        return 0

    tax = amount * tax_rate
    return tax


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)

    discount = calculate_discount(subtotal)

    amount = subtotal - discount

    tax = calculate_tax(amount, tax_rate)

    final_amount = amount + tax

    print("Subtotal:", subtotal, "Birr")
    print("Discount:", discount, "Birr")
    print("Tax:", tax, "Birr")
    print("Final Amount:", final_amount, "Birr")


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

tax_rate = 0.15

generate_receipt(items, tax_rate)
