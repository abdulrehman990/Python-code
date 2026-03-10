# Program no 1
""" info = {
    "Title" : "The Moon Rise",
    "author" : "Mickeal Jackson",
    "Price" : "1200",
    "Year" :  "2022"
}

print("Author :" , info["author"])
print("Price :", info["Price"])
"""
#Program no 2
"""
car = {
    "brand" : "Hyndai",
    "model" : "SUV" , 
    "Year" :   "2022"
}
print("Before Update : ", car.keys())
car.update({"color" : " White"})
print("After Update : ", car.keys())

"""

#Program no 3
"""
student = {
    "name": "Ahmed",
    "age": 21,
    "course": "Python"
}

print("It will print all of the keys in the students data" , " ",  student.keys())
print("It will print all of the Values in the students data" ,  " ", student.values())
print("It will print all of the items in the students data" , " ",   student.items())
"""
#Program no 4

student = {
    "age": 21
}
inp = input("Enter the key: ")

value = student.get(inp)

if value is None:
    print("Key not found")
else:
    print("Output:", value)