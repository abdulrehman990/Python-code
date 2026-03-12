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

#program no 8
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

print("It prints all the keys :", data.values())

#program no 9
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }

print("It prints all the keys :", data.items())

#program no 10
data = {
    "name" : "Abdul rehman",
    "age" : 29,
    "course" : "BSSE",
  }
val = input("Enter the value : ")
Value = data.get(val)
print("The data is" ,Value)

"""

#Program no 11
"""
numbers = [1,2,2,3,3,3]

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

#Program no 12
student_data = {
    
}
student_data.update({"Name" : "Abdul rehman"})
student_data.update({"Class" : "BSSE"})
student_data.update({"Roll_no" : 24399})
student_data.update({"Contact_no" : "0326 0781519"})

print(student_data)

#Program no 13
product = {
    "Shampoo" : 2000,
    "Sanitizer" : 200,
    "Bat" : 1200,
    "Books" : 200,

}
new = max(product.values())
if(new <= 1200 ):
    print("These are the most expensive things :" , max(product.keys()))
else:
    print("Not expensive")

#program no 14
coll = set()
print(type(coll))

#Program no 1
student = {
    "name": "Ali",
    "age": 21,
    "city": "Lahore"
}

vale = input("Enter the value : " )
name = student.get(vale)

if vale is None:
    print("Return nothing : ")
else:
  print("Print it ", name)
"""

product = {
    "name": "Laptop",
    "price": 50000
}

usesr = input("Enter the value : " )
product.update({"price" : usesr})
print(product)