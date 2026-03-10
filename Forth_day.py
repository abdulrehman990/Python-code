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
car = {
    "brand" : "Hyndai",
    "model" : "SUV" , 
    "Year" :   "2022"
}
print("Before Update : ", car.keys())
car.update({"color" : " White"})
print("After Update : ", car.keys())
