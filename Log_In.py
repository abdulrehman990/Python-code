print("**********Welcome to login form*************")

while True:
    email = input("Enter the Email: ")
    
    if "@" in email:
        print("Email added")
        break
    else:
        print("Invalid Email! Try again.")

while True:
     password = input("Enter the Password: ")
     if  not password.isalnum() and len(password) == 7:
        print("Welcome you have Logged in.")
        break
     elif(len(password) != 7 ):
         print("Your password must have at least 7 characters")
     else:
        print("Invalid Password! Try again.")
        print("Your password must have at least 7 characters and Special characters")


name = input("Enter the Name : ")
degree = input("Enter the Degree : ")
roll_no = input("Enter the Roll no : ")
marks = { "Math" : input("Enter you Math marks : " ),
         "English" : input("Enter you English marks : " ),
         "Physics" : input("Enter you Math marks :" ),}
total_marks = marks["English"] + marks["Math"] + marks["Physics"]
percentage = (total_marks / 100 ) * 100

if(percentage <= 80):
    "Grade A"
elif(percentage <= 70 and percentage >=79):
    "Grade B"
elif(percentage <= 60 and percentage >=69):
    "Grade C"
elif(percentage <= 50 and percentage >=59):
    "Grade D"
else:
    print("You are Fail!")


print ("Here's the student data:")
print(name)
print(degree)
print(roll_no)
print(marks)
print(percentage)
