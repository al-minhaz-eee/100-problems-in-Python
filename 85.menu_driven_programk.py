users_db = {}

def register():
    print("\n--- Register ---")
    username = input("Enter a username: ")

    if username in users_db:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    print(f"user {username} registered successfully!")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users_db and users_db[username] == password:
        print(f'Login successful! welcome, {username}.')
    else:
        print("Invalid username or password! Please try again.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Register ")
        print("2. Login")
        print("3. Exit")

        choice = input("choose an option (1/2/3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
menu()