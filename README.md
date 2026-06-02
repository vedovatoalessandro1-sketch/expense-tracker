# Expense Tracker

A simple Python program to keep track of your personal expenses, designed for absolute beginners.

## Features

- **Add expenses** with date, category, amount, and description
- **View all expenses** in a clean, formatted table
- **Filter expenses** by category
- **Summary** of total spending with percentage breakdown per category
- **Automatic saving** of data to a JSON file

## Project Structure

```
expense-tracker/
├── main.py               # Entry point — run this to start the program
├── expense_manager.py    # All the functions for managing expenses
├── expenses.json         # Created automatically on first run
├── .gitignore            # Files to exclude from Git
└── README.md             # This file
```

## Requirements

- Python 3.7 or higher
- No external libraries needed (uses only the standard library)

Check your Python version:
```bash
python --version
```

## Getting Started

1. **Clone or download** this repository to your preferred folder

2. **Navigate into** the project folder:
   ```bash
   cd expense-tracker
   ```

3. **Run the program:**
   ```bash
   python main.py
   ```

   On some systems you may need to use `python3`:
   ```bash
   python3 main.py
   ```

## How to Use

When you start the program, you will see this menu:

```
==========================================
       PERSONAL EXPENSE TRACKER
==========================================
  1. Add a new expense
  2. View all expenses
  3. Filter expenses by category
  4. Show summary and total
  5. Exit
==========================================
```

### Adding an expense (option 1)

The program will ask for:
- **Date**: press Enter to use today's date, or type `MM/DD/YYYY`
- **Category**: e.g. `Food`, `Transport`, `Entertainment`, `Health`, `Home`, `Clothing`, `Other`
- **Amount**: enter the value (e.g. `15.50` or `15,50`)
- **Description**: optional, press Enter to skip

### Example session

```
--- Add a new expense ---
Date [press Enter for today 06/02/2026, or MM/DD/YYYY]:
Available categories: Food, Transport, Entertainment, Health, Home, Clothing, Other
Category: food
Amount ($): 12.50
Short description (optional, press Enter to skip): Lunch with colleagues

Expense of $12.50 added successfully!
```

## Where is my data stored?

Data is automatically saved in `expenses.json` in the same folder as the program. You can open it with any text editor:

```json
[
  {
    "date": "06/02/2026",
    "category": "Food",
    "amount": 12.5,
    "description": "Lunch with colleagues"
  }
]
```

## Python concepts used in this project

If you are learning Python, here are the concepts you will find in the code:

| Concept | Where to find it |
|---|---|
| Functions (`def`) | All files |
| Lists and dictionaries | `expense_manager.py` |
| `while` and `for` loops | `main.py`, `expense_manager.py` |
| `if/elif/else` conditionals | Throughout the code |
| Error handling (`try/except`) | `add_expense` function |
| Reading/writing files | `load_expenses`, `save_expenses` |
| `json` module | `expense_manager.py` |
| `datetime` module | `expense_manager.py` |
| List comprehensions | `expense_manager.py` |
| f-strings | Throughout the code |

## Ideas for extending the project

Want to challenge yourself? Try adding:
- [ ] Delete an existing expense
- [ ] Edit an already recorded expense
- [ ] Filter by date range
- [ ] Export expenses to a CSV file (opens in Excel)
- [ ] Set a monthly budget per category with warnings

## License

Open source — free to use, modify, and share.
