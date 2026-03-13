#Program no 1
"""
i= 1
while i <=100:
    print("Counting" , i)
    i += 1

#Program no 2
i= 100
while i >=1:
    print("Counting" , i)
    i -= 1

#Program no 3
number = int(input("Enter the number : " ))
count = 1
while count <= 10 :
    print("The table of given no is :" , number ,"*" , count ,"=" , number * count)
    count += 1

#Program no 4
item = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(item) :
    print("list printed : ",item[index])
    index += 1
"""

item = [1,4,9,16,25,36,49,64,81,100]
x = 25
while item == x :
    print("list printed : ",item)
    x += 1