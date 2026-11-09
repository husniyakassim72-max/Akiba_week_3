def record_transaction(history, transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }
    history.append(transaction)


def deposit(balance, amount, history):
    if amount <= 0:
        print("Amount must be positive.")
        return balance

    balance += amount
    record_transaction(history, "deposit", amount, balance)
    print("Deposit successful.")
    return balance


def withdraw(balance, amount, history, daily_used, daily_limit):
    if amount <= 0:
        print("Amount must be positive.")
        return balance, daily_used

    if amount > balance:
        print("Not enough money.")
        return balance, daily_used

    if daily_used + amount > daily_limit:
        print("Daily withdrawal limit exceeded.")
        return balance, daily_used

    balance -= amount
    daily_used += amount

    record_transaction(history, "withdrawal", amount, balance)
    print("Withdrawal successful.")

    return balance, daily_used


def check_balance(balance):
    print("Current balance:", balance)


def transaction_summary(history):
    deposited = 0
    withdrawn = 0

    for transaction in history:
        if transaction["type"] == "deposit":
            deposited += transaction["amount"]
        else:
            withdrawn += transaction["amount"]

    print("Total deposited:", deposited)
    print("Total withdrawn:", withdrawn)
    print("Transaction history:")

    for transaction in history:
        print(transaction)


balance = 1000
daily_limit = 1000
daily_used = 0
history = []

balance = deposit(balance, 500, history)

balance, daily_used = withdraw(
    balance, 200, history, daily_used, daily_limit
)

check_balance(balance)
transaction_summary(history)