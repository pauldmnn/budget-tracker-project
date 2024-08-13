import json

def add_spending(spendings, description, amount):
    spendings.append({"description": description, "amount": amount})
    print(f"Added spending:{description}, Amount:{amount}")

def your_total_spendings(spendings):
    sum = 0
    for spending in spendings:
        sum += spending["amount"]
    return sum

def your_balance(budget, spendings):
    return budget - your_total_spendings(spendings)

def display_budget_details(budget, spendings):
    print(f"Total budget: {budget}")
    print("Spendings:")
    for spending in spendings:
        print(f"- {spending['description']}: {spending['amount']}")
    print(f"Total amount spent: {your_total_spendings(spendings)}")
    print(f"Your remaining budget to spend: {your_balance(budget, spendings)}")

def load_your_budget_data(filepath):
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
def save_your_budget(filepath, original_budget, spendings):
    data = {
        'original_budget': original_budget,
        'spendings': spendings
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
        original_budget = float(input("Please enter amount of money you have to spend: "))
    budget = original_budget
    
    while True:
        print("\n Choose what do you want to do.")
        print("1. Add spending")
        print("2. Display budget details")
        print("3. Exit")
        choice = input("Enter you choice (1/2/3): ")

        if choice == "1":
            description = input("Add spending description: ")
            amount = float(input("Enter spent amount: "))
            add_spending(spendings, description, amount)

        elif choice == "2":
            display_budget_details(budget, spendings)
        
        elif choice == "3":
            save_your_budget(filepath, original_budget, spendings)
            print("You are exiting your budget tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose one of the following options again (1/2/3).")

if __name__ == "__main__":
    main()