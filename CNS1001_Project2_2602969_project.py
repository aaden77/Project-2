# Used for reading and writing CSV files
import csv

# Dictionary used to store budget information
budget = {
    "monthly_budget": 0,  # User's monthly budget limit
    "total_income": 0,  # Running total of all income
    "total_expenses": 0  # Running total of all expenses
}

# Dictionary used to store category budgets and spending
categories = {

    # Food category
    "Food": {
        "budget": 0, # Amount allocated to Food
        "spent": 0  # Amount spent on Food
    },

    # Transportation category
    "Transport": {
        "budget": 0, # Amount allocated  to Transportation
        "spent": 0 # Amount spent on Transportation
    },

    # Bills category
    "Bills": {
        "budget": 0, # Amount allocated to Bills
        "spent": 0 # Amount spent on Bills
    },

    # Entertainment category
    "Entertainment": {
        "budget": 0, # Amount allocated to Entertainment
        "spent": 0 # Amount spent on Entertainment
    },

    # Savings category
    "Savings": {
        "budget": 0, # Amount allocated to Savings
        "spent": 0 # Amount spent on Savings
    }
}

# List used to store income and expense transactions
transactions = []

# Stores the user's savings target
savings_goal = 0

# Function that allows the user to set a monthly budget
def set_budget():

    # Keeps asking until a valid amount is entered
    while True:

        try:

            # Asks the user for their budget amount
            amount = float(input("Enter your monthly budget: $"))

            # Budget must be greater than zero
            if amount <= 0:
                print("Budget must be greater than $0.")

            else:

                # Stores budget in dictionary
                budget["monthly_budget"] = amount

                # Displays confirmation message
                print(f"Monthly budget set to ${amount:.2f}")

                # Exits loop
                break

        # Runs if user enters letters or symbols instead of numbers
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function that allows the user to set a savings goal
def set_savings_goal():

    # Allows the function to update the global savings goal variable.
    global savings_goal

    # Keep asking for input until a valid value is entered.
    while True:

        try:

            # Get the user's savings goal and converts it to a decimal number.
            goal = float(
                input("Enter your savings goal: $")
            )

            # Check if the savings goal is zero or negative.
            if goal < 0:

                # Tell the user that the goal must be positive.
                print(
                    "Savings goal must be not be less than $0."
                )

            else:

                # Save the valid goal amount.
                savings_goal = goal

                # Confirm the savings goal that was stored.
                print(
                    f"Savings goal set to "
                    f"${goal:.2f}"
                )

                # Exit the loop because valid input was received.
                break

        except ValueError:

            # Handle non-numeric input entered by the user.
            print(
                "Please enter a valid number."
            )

# Function allows users to allocate money to each spending category
def allocate_category_budget():

    print("\nAllocate Budget to Categories")

    # Loops through every category in the dictionary
    for category in categories:

        while True:

            try:

                # Asks user how much should be allocated
                amount = float(
                    input(f"Enter budget for {category}: $")
                )

                # Prevents negative numbers
                if amount < 0:
                    print("Amount cannot be negative.")

                else:

                    # Stores budget amount in category
                    categories[category]["budget"] = amount

                    # Exits loop once valid amount is entered
                    break

            except ValueError:

                # Handles letters or invalid symbols
                print("Please enter a valid number.")

    print("Category budgets allocated successfully.")

# Function records income transactions
def add_income():

    # Keeps asking for input until a valid amount is entered.
    while True:

        try:

            # Gets the income amount from the user.
            amount = float(input("Enter income amount: $"))

            # Checks if the income amount is negative.
            if amount < 0:

                # Informs the user that income cannot be less than zero.
                print("Income must not be less than $0.")

            else:

                # Adds the income amount to the total income.
                budget["total_income"] += amount

                # Stores the income transaction in the transaction history.
                transactions.append(
                    {
                        "type": "Income",
                        "amount": amount
                    }
                )

                # Confirms that the income was added successfully.
                print(f"Income of ${amount:.2f} added successfully.")

                # Exits the loop because valid input was received.
                break

        except ValueError:

            # Handle invalid input that cannot be converted to a number.
            print("Invalid amount entered.")

# Function records expenses and tracks category spending
def add_expense():

    print("\nExpense Categories:")

    # Displays all available categories
    for category in categories:
        print("-", category)

    # Asks user to choose category
    category = input(
        "Enter expense category: "
    ).title()

    # Verifies if category exists
    if category not in categories:
        print("Invalid category.")
        return

    while True:

        try:

            # Asks user for expense amount
            amount = float(
                input("Enter expense amount: $")
            )

            # Prevents negative values
            if amount <= 0:
                print("Expense must be greater than $0.")

            else:

                # Adds expense to overall expenses
                budget["total_expenses"] += amount

                # Adds expense to selected category
                categories[category]["spent"] += amount

                # Checks whether category budget has been exceeded
                if (
                    categories[category]["spent"]
                    >
                    categories[category]["budget"]
                ):

                    print(
                        f"WARNING: You have exceeded "
                        f"your {category} budget!"
                    )
                # Asks user for description of expense
                description = input("Enter expense description: ")

                # Saves transaction in transaction list
                transactions.append(
                    {
                        "type": "Expense",
                        "category": category,
                        "amount": amount,
                        "description": description
                    }
                )

                print(
                    f"Expense of ${amount:.2f} "
                    f"added to {category}."
                )

                break

        except ValueError:

            print("Invalid amount entered.")

# Function that displays all transactions
def view_transactions():

    # Checks if the transaction list is empty.
    if not transactions:

        # Informs the user that no transactions have been recorded.
        print("No transactions recorded.")

    else:

        # Displays a heading for the transaction history section.
        print("\n===== TRANSACTION HISTORY =====")

        # Loops through every transaction in the list.
        for transaction in transactions:

            # Checks if the current transaction is an expense.
            if transaction["type"] == "Expense":

                # Displays expense details including category and description.
                print(
                    f"{transaction['type']} "
                    f"({transaction['category']}) "
                    f"- ${transaction['amount']:.2f} "
                    f"| {transaction['description']}"
                )

            # Handles transactions that are not expenses.
            else:

                # Displays income details and amount.
                print(
                    f"{transaction['type']} "
                    f"- ${transaction['amount']:.2f}"
                )

# Function that displays spending information for all categories
def view_category_spending():

    print("\n===== CATEGORY REPORT =====")

    # Loops through each category
    for category, data in categories.items():

        # Calculates remaining category budget
        remaining = (
            data["budget"]
            -
            data["spent"]
        )

        print(
            f"{category}: "
            f"Budget=${data['budget']:.2f} | "
            f"Spent=${data['spent']:.2f} | "
            f"Remaining=${remaining:.2f}"
        )

# Function that displays budget summary
def view_budget_summary():

    # Calculates the remaining balance after expenses are deducted from income.
    remaining_balance = (
        budget["total_income"]
        - budget["total_expenses"]
    )

    # Displays a heading for the budget summary section.
    print("\n===== BUDGET SUMMARY =====")

    # Displays the monthly budget amount.
    print(
        f"Monthly Budget: ${budget['monthly_budget']:.2f}"
    )

    # Displays the total income recorded.
    print(
        f"Total Income: ${budget['total_income']:.2f}"
    )

    # Displays the total expenses recorded.
    print(
        f"Total Expenses: ${budget['total_expenses']:.2f}"
    )

    # Displays the remaining balance after expenses.
    print(
        f"Remaining Balance: ${remaining_balance:.2f}"
    )

# Function that displays progress towards savings goal
def view_savings_progress():

    # Checks if a savings goal has been set.
    if savings_goal == 0:

        # Informs the user that no savings goal exists.
        print(
            "No savings goal has been set."
        )

        # Exits the function because progress cannot be calculated.
        return

    # Gets the amount currently saved in the Savings category.
    current_savings = (
        categories["Savings"]["spent"]
    )

    # Calculates how much is left to reach the savings goal.
    remaining = (
        savings_goal
        - current_savings
    )

    # Calculates the percentage of the goal that has been achieved.
    percentage = (
        current_savings
        / savings_goal
    ) * 100

    # Displays a heading for the savings progress section.
    print(
        "\n===== SAVINGS PROGRESS ====="
    )

    # Displays the user's savings goal.
    print(
        f"Savings Goal: "
        f"${savings_goal:.2f}"
    )

    # Displays the amount saved so far.
    print(
        f"Saved So Far: "
        f"${current_savings:.2f}"
    )

    # Displays the percentage of the goal completed.
    print(
        f"Progress: "
        f"{percentage:.1f}%"
    )

    # Displays the remaining amount needed to reach the goal.
    print(
        f"Remaining To Goal: "
        f"${remaining:.2f}"
    )

    # Checks if the savings goal has been reached or exceeded.
    if current_savings >= savings_goal:

        # Congratulates the user for achieving the goal.
        print(
            "Congratulations! "
            "Savings goal achieved."
        )

# Function that saves all transaction records to a CSV file.
def save_transactions():

    # Opens file in write mode
    with open(
        "transactions.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Creates column headings
        writer.writerow(
            [
                "Type",
                "Category",
                "Amount",
                "Description"
            ]
        )

        # Writes transaction data
        for transaction in transactions:

            writer.writerow(
                [
                    transaction.get(
                        "type",
                        ""
                    ),

                    transaction.get(
                        "category",
                        ""
                    ),

                    transaction.get(
                        "amount",
                        ""
                    ),

                    transaction.get(
                        "description",
                        ""
                    )
                ]
            )

    print(
        "Transactions saved successfully."
    )

# Function that loads previously saved transaction records from a CSV file.
def load_transactions():

    try:

        # Clears existing records
        transactions.clear()

        # Opens CSV file
        with open(
            "transactions.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                transactions.append(
                    {
                        "type":
                        row["Type"],

                        "category":
                        row["Category"],

                        "amount":
                        float(row["Amount"]),

                        "description":
                        row["Description"]
                    }
                )

        print(
            "Transactions loaded successfully."
        )

    except FileNotFoundError:

        print(
            "No saved transactions found."
        )

# Main function controls the overall flow of the program
def main():

    # Variable keeps program running
    running = True

    while running:

        # Displays menu
        print("1. Set Monthly Budget")
        print("2. Set Savings Goal")
        print("3. Allocate Category Budgets")
        print("4. Add Income")
        print("5. Add Expense")
        print("6. View Transactions")
        print("7. View Category Spending")
        print("8. View Budget Summary")
        print("9. View Savings Progress")
        print("10. Save Transactions")
        print("11. Load Transactions")
        print("12. Exit")

        # Gets user's menu selection
        choice = input("\nEnter your choice: ")

        if choice == "1":

            # Opens budget setup
            set_budget()

        elif choice == "2":

            # Opens savings goal setup
            set_savings_goal()

        elif choice == "3":

            # Opens category budget allocation
            allocate_category_budget()

        elif choice == "4":

            # Opens income recording function
            add_income()

        elif choice == "5":

            # Opens expense recording function
            add_expense()

        elif choice == "6":

            # Displays transaction history
            view_transactions()

        elif choice == "7":

            # Displays category spending report
            view_category_spending()

        elif choice == "8":

            # Displays overall budget summary
            view_budget_summary()

        elif choice == "9":

            # Displays savings goal progress
            view_savings_progress()

        elif choice == "10":

            # Saves all recorded transactions to a CSV file.
            save_transactions()

        elif choice == "11":

            # Loads previously saved transactions from a CSV file.
            load_transactions()

        elif choice == "12":

            # Exits the program
            running = False

            print(
                "Thank you for using Budget Tracker."
            )

        else:

            # Handles invalid menu selections.
            print("Invalid choice. Please try again.")

# Starts the program by calling the main function
main()
