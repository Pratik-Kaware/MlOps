class chatbook:
    #constructor which initialize 3 attributes and called a method
    def __init__(self):
        print("Chatbook class initialize")
        self.username = ''
        self.password = ''
        self.loggedin = False               # keeping it false so that user cannot do step 3,4,5 
        self.menu()

    #method which asks for user input

    def menu(self):
        user_input = input("""Welcome to the chatbook !!! How would you like to proceed ?
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
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    # Signup method
    def signup(self):
        email = input("Please enter your email ID here --->")
        pwd = input("Please submit your password here")
        self.username = email
        self.password = pwd
        print("You've signed up successfully!\n")
        self.menu()

    # SignIn method
    def signin(self):
        if self.username == '' and self.password == '':   # if username and password does not exist
            print("No account found. Please sign up first.")
        else:                                                           #checking if the entered values are same as the one entered in step 1
            uname = input("Please enter your email ID here --->")
            pwd = input("Please submit your password here")
            if self.username == uname and self.password == pwd:
                print("You have signed successfully !!!!")
                self.loggedin = True                       # loggedin set to true so that user can start posting and stuff only if creds are correct
            else:
                print("Please input correct credential....")
        print("\n")
        self.menu()

    # My-post method
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter you Post here--->\n")
            print(f"Following content has been post {txt}")
        else:
            print("You need to sign in first")
            print("\n")
        self.menu()

    # Message method
    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Input your message here --->\n")
            frnd = input("Whom you want to send message to ? ")
            print(f"Your message {txt} was sent to {frnd}")
        else:
            print("You need to login first \n")
            self.menu()

        
obj = chatbook()

                        



            





