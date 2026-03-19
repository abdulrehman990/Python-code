print("**********Welcome to login form*************")

while True:
    email = input("Enter the Email: ")
    
    if "@" in email:
        print("Now Press Enter to put password.")
        break
    else:
        print("Invalid Email! Try again.")

while True:
     password = input("Enter the Password: ")
     if  not password.isalnum() and len(password) == 7:
        print("Welcome you have Logged in.")
        break
     else:
        print("Invalid Password! Try again.Your password must have at least 7 characters")      