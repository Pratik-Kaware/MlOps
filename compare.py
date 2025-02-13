class ChatBook:
    # Constructor initializes attributes and calls the menu method
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False  # Prevents unauthorized actions
        self.menu()

    # Method to display the menu and handle user input
    def menu(self):
        user_input = input("""Welcome to the chatbook!!! How would you like to proceed?
        1. Press 1 to sign up
        2. Press 2 to sign in
        3. Press 3 to write a post
        4. Press 4 to message a friend
        5. Press any other key to exit
        Your choice: """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            if self.loggedin:
                print("You can now write a post!")
            else:
                print("You must sign in first.")
        elif user_input == "4":
            if self.loggedin:
                print("You can now message a friend!")
            else:
                print("You must sign in first.")
        else:
            print("Exiting ChatBook. Goodbye!")
            exit()

    # Signup method
    def signup(self):
        email = input("Please enter your email ID: ")
        pwd = input("Please create a password: ")
        self.username = email
        self.password = pwd
        print("You've signed up successfully!\n")
        self.menu()

    # Signin method
    def signin(self):
        if self.username == '' and self.password == '':  # If no account exists
            print("No account found. Please sign up first.")
        else:
            uname = input("Enter your email ID: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!")
                self.loggedin = True  # User is now logged in
            else:
                print("Incorrect credentials. Please try again.")
        print("\n")
        self.menu()


# Creating an object of the class to run the application
obj = ChatBook()
