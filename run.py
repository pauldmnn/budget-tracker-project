import json


def add_spending(spendings, description, amount):
    """
    For the user to input the description of spendings
    and amount of spendings
    """
    spendings.append({"description": description, "amount": amount})
    print(f"Added spending:{description}, Amount:{amount}")


def your_total_spendings(spendings):
    """
    Sums up the total amount of spendings
    """
    sum = 0
    for spending in spendings:
        sum += spending["amount"]
    return sum


def your_balance(budget, spendings):
    return budget - your_total_spendings(spendings)


def display_budget_details(budget, spendings):
    """
    The user to input their budget amount from which all
    spendings will be deducted
    """
    print(f"Total budget: {budget}")
    print("Spendings:")
    for spending in spendings:
        print(f"- {spending['description']}: {spending['amount']}")
    print(f"Total amount spent: {your_total_spendings(spendings)}")
    print(f"Your remaining budget to spend: {your_balance(budget, spendings)}")


def load_your_budget_data(filepath):
    """
    Loads the budget and spendings amount into a file so
    when the app is refreshed the data is not lost.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['original_budget'], data['spendings']

    except (FileNotFoundError, json.JSONDecodeError):
        """
        Return default values if the file doesn't exist
        or is empty/corrupted
        """
        return 0, []


def update_your_budget(filepath, original_budget, spendings):
    """
    Updates the budget when choice 3 is selected
    """
    data = {
        'original_budget': original_budget,
        'spendings': spendings
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def save_your_budget(filepath, original_budget, spendings):
    """
    Saves the data to the json file
    """
    data = {
        'original_budget': original_budget,
        'spendings': spendings
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def reset_budget(filepath):
    """
    Resets the JSON file to make the budget and spendigs to zero
    """
    main_budget = 0
    main_spendings = []
    data = {
        'original_budget': main_budget,
        'spendings': main_spendings
        }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """
    Runs the main function for the app
    """
    print("Welcome to your budget tracker")
    filepath = 'your_budget_data.json'
    original_budget, spendings = load_your_budget_data(filepath)
    if original_budget == 0:
        original_budget = float(input("Please enter amount to spend: \n"))
        try:
            original_budget = float(input("Please enter amount to spend: \n"))
        except ValueError:
            print("Wrong input. Please enter a valid number")
    budget = original_budget

    while True:
        print("\n Choose what do you want to do.")
        print("1. Add spending type and amount")
        print("2. Display budget details")
        print("3. Add more money to budget")
        print("4. Reset the tracker and startb again")
        print("5. Exit the tracker")
        choice = input("Enter you choice (1/2/3/4/5): \n")

        if choice == "1":
            description = input("Add spending description: \n")
            amount = float(input("Enter spent amount:£ \n"))
            add_spending(spendings, description, amount)

        elif choice == "2":
            display_budget_details(budget, spendings)

        elif choice == "3":
            more_budget = float(input("Add more amount to budget:£ \n"))
            original_budget += more_budget
            budget = original_budget
            update_your_budget(filepath, original_budget, spendings)
            print(f"Added £{more_budget} to original budget."
                  f"New budget £{original_budget}")

        elif choice == "4":
            reset_budget(filepath)
            original_budget, spendings = load_your_budget_data(filepath)
            budget = original_budget
            print("Budget and spendings have been reset")

        elif choice == "5":
            save_your_budget(filepath, original_budget, spendings)
            print("You are exiting your budget tracker. Goodbye!")
            break

        else:
            print("Wrong choice. Choose one of the following (1/2/3/4/5).")


if __name__ == "__main__":
    main()
