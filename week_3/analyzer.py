def add_expense(expenses, description, category, amount):
    if description.strip() == "" or category.strip() == "":
        print("Description and category cannot be empty.")
        return

    if amount <= 0:
        print("Amount must be positive.")
        return

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


def largest_expense(expenses):
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above(expenses, threshold=200):
    for expense in expenses:
        if expense["amount"] > threshold:
            print(expense)


def spending_report(expenses, threshold=200):
    total = total_expenses(expenses)
    categories = spending_by_category(expenses)

    print("Total expenses:", total, "Birr")

    print("\nSpending by category:")

    for category in categories:
        percentage = categories[category] / total * 100
        print(
            category,
            ":", categories[category], "Birr,",
            round(percentage, 2), "%"
        )

    largest = largest_expense(expenses)

    if largest is not None:
        print("\nLargest expense:", largest)

    if categories:
        highest_category = max(categories, key=categories.get)
        print("Highest spending category:", highest_category)
        print("Category total:", categories[highest_category], "Birr")

    print("\nExpenses above", threshold, "Birr:")
    expenses_above(expenses, threshold)


expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

add_expense(expenses, "Notebook", "Education", 80)

spending_report(expenses)