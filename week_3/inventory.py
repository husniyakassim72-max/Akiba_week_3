def add_product(products, name, price, stock):
    if name.strip() == "":
        print("Product name cannot be empty.")
        return

    if name in products:
        print("Product already exists.")
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    products[name] = {
        "price": price,
        "stock": stock
    }

    print("Product added.")


def search_product(products, name):
    if name in products:
        print(products[name])
    else:
        print("Product not found.")


def update_price(products, name, new_price):
    if name not in products:
        print("Product not found.")
    elif new_price < 0:
        print("Price cannot be negative.")
    else:
        products[name]["price"] = new_price
        print("Price updated.")


def increase_stock(products, name, quantity):
    if name not in products:
        print("Product not found.")
    elif quantity <= 0:
        print("Quantity must be positive.")
    else:
        products[name]["stock"] += quantity
        print("Stock increased.")


def sell_product(products, name, quantity):
    if name not in products:
        print("Product not found.")
    elif quantity <= 0:
        print("Quantity must be positive.")
    elif quantity > products[name]["stock"]:
        print("Not enough stock.")
    else:
        products[name]["stock"] -= quantity
        print("Sale successful.")


def inventory_value(products):
    total = 0

    for name in products:
        total += products[name]["price"] * products[name]["stock"]

    return total


def low_stock_report(products, threshold=5):
    for name in products:
        if products[name]["stock"] < threshold:
            print(name, products[name]["stock"], "units left")


products = {}

add_product(products, "Book", 100, 10)
add_product(products, "Pen", 20, 3)

search_product(products, "Book")
update_price(products, "Book", 120)
increase_stock(products, "Pen", 2)
sell_product(products, "Book", 2)

print("Total inventory value:", inventory_value(products))

print("Low-stock products:")
low_stock_report(products)