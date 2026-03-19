print("**********Welcome to login form*************")

while True:
    email = input("Enter the Email: ")
    
    if "@" in email:
        print("Now Press Enter to put password.")
        break
    else:
        print("Invalid Email! Try again.")

password = input("Enter the Password: ")
if  "$" in password:
        print("Welcome you have Logged in.")
else:
        print("Invalid Password! Try again.")
      