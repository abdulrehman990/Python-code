
# Program no 1
first_name = input("Enter the first name = ")

print(first_name)
print(len(first_name))

# Program no 2
first = "I bought a car in $  in usa of $22191"
print(first.count("$"))

mark = int( input("Enter the marks"))
if(mark >= 80):
    grade = "A"
elif(mark >= 70 and mark < 80):
        grade = "B"

elif(mark >= 60 and mark < 70):
        grade = "C"

elif(mark >= 50 and mark < 60 ):
       grade = "D"

else:
      grade = "F"

print("Grade of the students", grade)


# Program no 3
num= int( input("Enter the Number"))

if(num % 2 == 0):
    print("Number is even")

else:
    print("Number is odd")

# Program no 4
num1 = int( input("Enter the Number"))
num2 = int( input("Enter the Number"))
num3 = int( input("Enter the Number"))

if (num1 > num2 and num3):
    print("Num1 is greater then num2 and num3")
elif (num1 >= num2 and num3):
    print("Num1 is equal to num2 and num3")
else:
    print("Num1 is smaller than num2 and num3")


# Program no 5
num= int( input("Enter the Number"))

if(num % 7 == 0):
    print("Multiple of 7")

else:
    print("Not a Multiple of 7")


    