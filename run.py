def add_spending(spendings, description, amount):
    spendings.append({"description": description, "amount": amount})
    print(f"Added spending:{description}, Amount:{amount}")

def main():
    """
    Runs the main function for the app
    """
    print("Welcome to your budget tracker")
    original_budget = float(input("Please enter your original spending budget: "))
    budget = original_budget
    spendings = []

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
            print("You are exiting your budget tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose one of the following options again (1/2/3).")

if __name__ == "__main__":
    main()