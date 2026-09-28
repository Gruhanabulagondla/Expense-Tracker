import json
import os

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    total = 0

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_total(expenses):
    category = input("Enter category: ").lower()

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category:
            total += expense["amount"]

    print(f"Total spent on {category}: ₹{total:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            expenses.pop(number - 1)
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Enter a valid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Total")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            category_total(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()