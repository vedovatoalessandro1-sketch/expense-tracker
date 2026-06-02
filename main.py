# =============================================================================
# main.py
# This is the main entry point of the program. Everything starts here.
# Run this file with: python main.py
#
# Project structure:
#   main.py              <- (this file) handles the menu and startup
#   expense_manager.py   <- contains all the functions for managing expenses
#   expenses.json        <- created automatically to store your data
# =============================================================================

# "import" loads code from another Python file
# We only import the functions we actually need from expense_manager.py
from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    filter_by_category,
    show_summary
)


def show_menu():
    """Prints the main menu to the terminal."""
    print("\n" + "=" * 42)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 42)
    print("  1. Add a new expense")
    print("  2. View all expenses")
    print("  3. Filter expenses by category")
    print("  4. Show summary and total")
    print("  5. Exit")
    print("=" * 42)


def main():
    """
    Main function of the program.
    Loads the data, shows the menu, and calls the right function
    based on the user's choice.
    """
    print("Welcome to Personal Expense Tracker!")
    print("Your data is saved automatically.")

    # Load existing expenses from the JSON file right away.
    # If it's the first run, the list will be empty [].
    expenses = load_expenses()

    if expenses:
        print(f"(Loaded {len(expenses)} expenses from previous session)")

    # The main program loop: keeps running until the user chooses "5"
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # add_expense returns the updated list
            expenses = add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            filter_by_category(expenses)

        elif choice == "4":
            show_summary(expenses)

        elif choice == "5":
            print("\nGoodbye! Your data has been saved.")
            break  # "break" exits the while loop and the program ends

        else:
            # The user entered something other than 1-5
            print("Invalid choice. Please enter a number from 1 to 5.")


# This block is the standard Python entry point.
# "__name__ == '__main__'" is True only when we run this file directly
# (not when it is imported by another file).
if __name__ == "__main__":
    main()
