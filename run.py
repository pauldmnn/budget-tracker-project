import json
import re

def is_number(input_str):
    """
    Checks if the input is a valid number
    """
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def description_is_correct(input_str):
    """
    Checks that the input for description uses only letters and spaces
    """
    return bool(re.match("^[A-Za-z ]+$",
                input_str)) and input_str.strip() != ''


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
    print(f"Your remaining budget to spend is: {your_balance(budget, spendings)} \n")


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
    print("Welcome to your budget tracker \n")
    filepath = 'your_budget_data.json'
    original_budget, spendings = load_your_budget_data(filepath)
    if original_budget == 0:
        while True:
            original_budget_input = input("Please enter amount to spend: \n")
            if is_number(original_budget_input):
                original_budget = float(original_budget_input)
                break
            else:
                print("\n Your entry is wrong. Please enter a valid number \n")
    budget = original_budget

    while True:
        print("\n Choose what do you want to do. \n")
        print("1. Add spending type and amount")
        print("2. Display budget details")
        print("3. Add more money to budget")
        print("4. Reset the tracker and start again")
        print("5. Exit the tracker \n")
        choice = input("\n Enter you choice (1/2/3/4/5): \n")

        if choice == "1":
            while True:
                description = input("Using letters, please add a description of your spendings: \n")
                if description_is_correct(description):
                    break
                else:
                    print("\n Please enter description using letters only \n")
            while True:
                amount_input = input("Enter spent amount:£ \n")
                if is_number(amount_input):
                    amount = float(amount_input)
                    break
                else:
                    print("\n Please enter a valid number \n")
            add_spending(spendings, description, amount)

        elif choice == "2":
            display_budget_details(budget, spendings)

        elif choice == "3":
            while True:
                more_budget_input = input("Add more amount to budget:£ \n")
                if is_number(more_budget_input):
                    more_budget = float(more_budget_input)
                    break
                else:
                    print("\n Please enter a valid number \n")
            original_budget += more_budget
            budget = original_budget
            update_your_budget(filepath, original_budget, spendings)
            print(f"Added £{more_budget} to original budget."
                  f"New budget £{original_budget}")

        elif choice == "4":
            reset_budget(filepath)
            original_budget, spendings = load_your_budget_data(filepath)
            budget = original_budget
            print("\n Budget and spendings have been reset \n")

        elif choice == "5":
            save_your_budget(filepath, original_budget, spendings)
            print("\n You are exiting your budget tracker. Goodbye! \n")
            break

        else:
            print("\n Wrong choice. Choose one of the following (1/2/3/4/5). \n")


if __name__ == "__main__":
    main()
