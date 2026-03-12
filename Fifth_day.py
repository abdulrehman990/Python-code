"""
Program no 1
student = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

print(  
student.values()
)
#program no 2
students = {
    "Abdul rehman" : 90,
    "Al Rayyan" : 92,
    "Taha raza" :91
}
print("Marks of the students are: " , students.values())

#program no 4
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

user = input("Enter the value : " )
value = data.get(user)


if user is None:
    print("Error")
else:
    print("value : ", value)

"""