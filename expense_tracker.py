import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    """Load expense entries from a JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """Save expense entries to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category, description):
    """Record a new expense."""
    expenses = load_expenses()
    entry = {
        "id": len(expenses) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": round(float(amount), 2),
        "category": category.strip().title(),
        "description": description.strip()
    }
    expenses.append(entry)
    save_expenses(expenses)
    print(f"\nExpense of ₹{entry['amount']} under '{entry['category']}' recorded.")

def view_expenses():
    """List all recorded expenses."""
    expenses = load_expenses()
    if not expenses:
        print("\nNo expense records found.")
        return

    print("\n--- All Recorded Expenses ---")
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<25}")
    print("-" * 70)
    for exp in expenses:
        print(f"{exp['id']:<5} {exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:<9.2f} {exp['description']:<25}")
    print("-" * 70)

def show_summary():
    """Display category-wise breakdown and total expenditure."""
    expenses = load_expenses()
    if not expenses:
        print("\nNo data to analyze.")
        return

    total_spent = sum(item["amount"] for item in expenses)
    category_totals = {}

    for item in expenses:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + item["amount"]

    print("\n--- Expenditure Summary ---")
    print(f"Total Spent: ₹{total_spent:.2f}\n")
    print(f"{'Category':<18} {'Amount':<12} {'Percentage':<10}")
    print("-" * 42)
    for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        pct = (total / total_spent) * 100 if total_spent > 0 else 0
        print(f"{cat:<18} ₹{total:<11.2f} {pct:>5.1f}%")
    print("-" * 42)

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. View All Expenses")
        print("2. Add New Expense")
        print("3. View Category Summary & Total")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            view_expenses()
        elif choice == "2":
            try:
                amount_input = float(input("Enter amount: ").strip())
                if amount_input <= 0:
                    print("Amount must be greater than zero.")
                    continue
                category = input("Enter category (e.g., Food, Travel, Books, Utilities): ").strip()
                description = input("Enter brief description: ").strip()
                if category:
                    add_expense(amount_input, category, description)
                else:
                    print("Category is required.")
            except ValueError:
                print("Invalid input. Please enter a valid number for amount.")
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
