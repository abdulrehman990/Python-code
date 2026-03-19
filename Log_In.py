print("**********Welcome to login form*************")

while True:
    email = input("Enter the Email: ")
    
    if "@" in email:
        print("Now Press Enter to put password.")
        break
    else:
        print("Invalid Email! Try again.")
      