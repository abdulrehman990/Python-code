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

item = [1,4,9,16,25,36,49,64,81,25,100]
index = 0
x=25
while index < len(item) :
    if item[index] == x:
        print("list printed : ",index)
    index += 1

i = 1
total = 0

while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

print("Sum of even numbers:", total)

#What does the following Python code do?

count = 0
while count < 5:
   print("Count:", count)
   count += 1
   if count == 3:
       continue
   print("After Continue")
"""
#program no 10
new = input("Enter the word : ")
dig = new.isalpha()
while not dig :
    print("The character in this is not a word")
    new1 = input("Enter the word : ")
    print(len(new1))