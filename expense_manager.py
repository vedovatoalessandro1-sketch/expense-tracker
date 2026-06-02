# =============================================================================
# expense_manager.py
# Contains all the functions for managing personal expenses.
# Each function does one thing only — this is called the "single responsibility
# principle" and is a good programming habit.
# =============================================================================

import json       # For reading and writing JSON files
import os         # For checking if a file exists
from datetime import datetime  # For getting today's date

# Name of the file where we save the data.
# Changing this variable changes the file used throughout the whole program.
EXPENSES_FILE = "expenses.json"


def load_expenses():
    """
    Reads expenses from the JSON file and returns them as a list.
    If the file doesn't exist yet, returns an empty list [].
    """
    # os.path.exists() checks whether a file exists on disk
    if not os.path.exists(EXPENSES_FILE):
        return []  # First time running the program: no expenses yet

    # Open the file in read mode ("r")
    # encoding="utf-8" handles special characters correctly (é, ü, ñ...)
    with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)  # json.load() converts JSON into a Python list


def save_expenses(expenses):
    """
    Saves the list of expenses to the JSON file on disk.
    Called every time a new expense is added.
    """
    # Open the file in write mode ("w") — overwrites existing content
    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        # json.dump() converts the Python list into JSON format
        # ensure_ascii=False allows saving special characters
        # indent=2 makes the JSON file human-readable with 2-space indentation
        json.dump(expenses, file, ensure_ascii=False, indent=2)


def add_expense(expenses):
    """
    Asks the user for the details of a new expense via the terminal,
    adds it to the list, and saves everything to disk.
    Returns the updated list.
    """
    print("\n--- Add a new expense ---")

    # --- DATE ---
    # Show today's date as a default suggestion
    today = datetime.today().strftime("%m/%d/%Y")  # strftime formats the date as a string
    date_input = input(f"Date [press Enter for today {today}, or MM/DD/YYYY]: ").strip()

    # .strip() removes leading and trailing whitespace
    if date_input == "":
        date = today  # User pressed Enter: use today's date
    else:
        date = date_input

    # --- CATEGORY ---
    valid_categories = ["Food", "Transport", "Entertainment", "Health", "Home", "Clothing", "Other"]
    print("Available categories: " + ", ".join(valid_categories))
    category = input("Category: ").strip().capitalize()  # .capitalize() makes the first letter uppercase

    # --- AMOUNT ---
    # Use a while loop to repeat the prompt if the user enters an invalid value
    while True:
        try:
            # .replace(",", ".") allows writing both "15,50" and "15.50"
            amount_input = input("Amount ($): ").strip().replace(",", ".")
            amount = float(amount_input)  # Convert the string to a decimal number

            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue  # Go back to the start of the while loop

            break  # Exit the loop: the amount is valid
        except ValueError:
            # ValueError is raised if float() can't convert the string
            print("Invalid value. Please enter a number (e.g. 15.50 or 15,50).")

    # --- DESCRIPTION ---
    description = input("Short description (optional, press Enter to skip): ").strip()

    # --- CREATE THE EXPENSE ---
    # A Python dictionary is a collection of key-value pairs
    new_expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    # .append() adds an element to the end of the list
    expenses.append(new_expense)

    # Save immediately to disk so no data is lost
    save_expenses(expenses)

    print(f"\nExpense of ${amount:.2f} added successfully!")  # :.2f shows 2 decimal places
    return expenses


def view_expenses(expenses):
    """
    Displays all recorded expenses in a readable table in the terminal.
    """
    if not expenses:  # Empty list = no expenses
        print("\nNo expenses recorded yet.")
        return  # Exit the function without doing anything else

    print("\n--- All recorded expenses ---")

    # Print the table header
    # :<4 left-aligns in 4 characters, :>9 right-aligns in 9 characters
    print(f"{'#':<4} {'Date':<12} {'Category':<16} {'Amount':>9}  Description")
    print("-" * 62)

    # enumerate() gives us both the index and the element of the list
    # start=1 makes the counter start from 1 instead of 0
    for i, expense in enumerate(expenses, start=1):
        # If the description is empty, show "-"
        description = expense.get("description") or "-"
        print(f"{i:<4} {expense['date']:<12} {expense['category']:<16} ${expense['amount']:>8.2f}  {description}")

    print("-" * 62)
    # Calculate total using a list comprehension (compact way to iterate a list)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total':>34} ${total:>8.2f}")
    print(f"\nTotal expenses recorded: {len(expenses)}")


def filter_by_category(expenses):
    """
    Shows only expenses belonging to a category chosen by the user.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    # set() removes duplicates, sorted() sorts alphabetically
    available_categories = sorted(set(e["category"] for e in expenses))

    print("\nCategories found in your expenses:")
    for i, cat in enumerate(available_categories, start=1):
        print(f"  {i}. {cat}")

    chosen_category = input("\nWhich category would you like to see? ").strip().capitalize()

    # Filter the list using a list comprehension
    # Keep only expenses whose category matches the chosen one
    filtered = [e for e in expenses if e["category"] == chosen_category]

    if not filtered:
        print(f"\nNo expenses found for category '{chosen_category}'.")
        print(f"Available categories: {', '.join(available_categories)}")
        return

    print(f"\n--- Expenses for category: {chosen_category} ---")
    print(f"{'#':<4} {'Date':<12} {'Amount':>9}  Description")
    print("-" * 45)

    for i, expense in enumerate(filtered, start=1):
        description = expense.get("description") or "-"
        print(f"{i:<4} {expense['date']:<12} ${expense['amount']:>8.2f}  {description}")

    print("-" * 45)
    total = sum(e["amount"] for e in filtered)
    print(f"Total {chosen_category}: ${total:.2f}  ({len(filtered)} expenses)")


def show_summary(expenses):
    """
    Shows the grand total and a breakdown of expenses grouped by category,
    including the percentage each category represents of the total.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Expense summary by category ---")

    # Build a dictionary with the total for each category
    by_category = {}
    for expense in expenses:
        cat = expense["category"]
        # If the category isn't in the dictionary yet, initialize it to 0
        if cat not in by_category:
            by_category[cat] = 0.0
        by_category[cat] += expense["amount"]

    # Sort categories by amount from highest to lowest
    # key=lambda x: x[1] sorts by the second element of the pair (the total)
    # reverse=True sorts in descending order
    sorted_categories = sorted(by_category.items(), key=lambda x: x[1], reverse=True)

    grand_total = sum(e["amount"] for e in expenses)

    print(f"\n{'Category':<20} {'Amount':>10}  {'% of total':>11}")
    print("-" * 47)

    for category, total in sorted_categories:
        percentage = (total / grand_total) * 100
        # Print a visual bar proportional to the percentage
        bar = "█" * int(percentage / 5)
        print(f"{category:<20} ${total:>9.2f}  {percentage:>6.1f}%  {bar}")

    print("-" * 47)
    print(f"{'GRAND TOTAL':<20} ${grand_total:>9.2f}  {'100.0%':>11}")
    print(f"\nTotal number of expenses: {len(expenses)}")
