# Program no 1
""" movies = input("Enter your favourite movie name: ")
movies1 = input("Enter your favourite movie name: ")
movies2 = input("Enter your favourite movie name: ")
print(movies)
print(movies1)
print(movies2)

movie_list = []
movie_list.append(movies)
movie_list.append(movies1)
movie_list.append(movies2)

print(movie_list) """

#Program no 2

""" palidorm = [1,3,3,1]
palidorm1 = palidorm.copy()
palidorm1.reverse()
print(palidorm)
if(palidorm1 == palidorm):
    print("You are right")
else:
    print("Not")"""

#Program no 3
"""
tuple = ("A","C","A","B","A","F","A","E","D")

tuple2= tuple.count("A")
print(tuple2)

list = ["A","C","A","B","A","F","A","E","D"]
print(list.sort())
print(list)
"""

#Program no 4
"""
name = input("Enter the name : ")
age = input("Enter the age : ")
course = input("Enter the course : ")

print("My name is ",name)
print("I am" ,age ,"old")
print("I study" , course)
"""
#Program no 5
"""
username = input("Enter the username : ")
if(username[0] == "A"):
 print("Premium User")
elif(username[0] == "B"):
 print("Standard user")
else:
 print("Guest user")
 """

#Program no 6
"""                                             
list = ["milk", "bread", "eggs", "butter", "rice"]

print(list[0])
print(list[4])
print(list[0:3])
    """
#Program no 7
password = input("Enter the Password : ")

if(len(password) <= 6 ):
    print("Weak password")
elif(password.find("@") or password.find("$")):
    print("Strong password")
else:
    print("standard password")