
print()
print("**********Welcome to login form*************")
print()
while True:
    email = input("Enter the Email: ")
    
    if "@" in email:
        print("Email added")
        break
    else:
        print("Invalid Email Format! Try again.")

while True:
     password = input("Enter the Password: ")
     if  not password.isalnum() and len(password) >= 7:
        print()
        print("**********Welcome you have Logged in.**********")
        print()
        break
     elif(len(password) != 7 ):
         print("Your password must have at least 7 characters")
     else:
        print("Invalid Password! Try again.")
        print("Your password must have at least 7 characters and Special characters")

name = input("Enter the Name : ")
degree = input("Enter the Degree : ")
roll_no = input("Enter the Roll no : ")
print()
marks = {
    "Math": int(input("Enter your Math marks: ")),
    "English": int(input("Enter your English marks: ")),
    "Physics": int(input("Enter your Physics marks: "))
}

total_marks = marks["Math"] + marks["English"] + marks["Physics"]

percentage = (total_marks / 300) * 100

print()
print ("**********Here's the student data.**********")
print()
print(name)
print(degree)
print(roll_no)
print(marks.items())
print(percentage)

if(percentage >= 80):
    print("Grade A")
elif(percentage <= 70 and percentage >=79):
    print("Grade B")
elif(percentage <= 60 and percentage >=69):
    print("Grade C")
elif(percentage <= 50 and percentage >=59):
    print("Grade D")
else:
    print("You are Fail!")

print()
print("**********Stores student data in list for University record**********")
print()
student = {
    "name": name,
    "degree": degree,
    "roll_no": roll_no,
    "marks": marks,
    "percentage": percentage
}

students = []
students.append(student)
print(students)
print()
print()
print()
