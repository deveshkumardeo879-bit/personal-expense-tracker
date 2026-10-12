import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (DD-MM-YYYY): ").strip()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number for the amount.")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    total = 0

    for row in rows:
        date, category, amount, description = row
        print(
            f"Date: {date} | "
            f"Category: {category} | "
            f"Amount: ₹{float(amount):.2f} | "
            f"Description: {description}"
        )
        total += float(amount)

    print("----------------------------------")
    print(f"Total Expenses: ₹{total:.2f}")


def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("Total Expenses: ₹0.00")
        return

    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    summary = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            summary[category] = summary.get(category, 0) + amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n====================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("====================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()