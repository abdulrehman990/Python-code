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

#program no 3
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

  #program no 4
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }
print("The data before update :",data)
data.update({"age" : 49})
print("The data after update :",data)

#Program no 5
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }
print("The data before update :",data)
data.update({"City" : "Faisalabad"})
print("The data after update :",data)

#program no 6
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }
print("The data before pop :",data)
data.pop("age")
print("The data after pop :",data)

#program no 7
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

print("It prints all the keys :", data.keys())

"""
#program no 7
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

print("It prints all the keys :", data.values())
