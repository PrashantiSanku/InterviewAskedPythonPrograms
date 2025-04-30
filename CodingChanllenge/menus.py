def display_menu():
    print("1. Start Game")
    print("2. Load Game")
    print("3. Options")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    try:
        return int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return display_menu()