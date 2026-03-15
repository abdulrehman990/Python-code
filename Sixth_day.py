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

#program no 10
new = input("Enter the word : ")
dig = new.isalpha()
while not dig :
    print("The character in this is not a word")
    new1 = input("Enter the word : ")
    print(len(new1))

#Program no 11
numbers = [12, 45, 7, 89, 34, 23]

index = 0
maximum = numbers[0]

while index < len(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]

    index += 1

print("The maximum number in the list is:", maximum)

#program no 13
items = ["pen", "book", "laptop", "mobile", "bag"]

index = 0
new = input("Enter the Word : ")
while index < len(items):
    if new == items[index] :
        print("The value is present", )
        break 
    index += 1
    
else:
     print("The value is not present")

     
#PROGRAM NO 10
numbers = [3, 8, 15, 20, 7, 12, 10]
index = 0
count = 0
while index < len(numbers):
    if numbers[index] % 2 == 0 :
        
        print("Even no",numbers[index] )
        count +=1 

    index += 1

print("The Even no in the list is ", count )
"""
#program no 18
password = "admin123"

new = input("Enter the password: ")

while new != password:
    print("Incorrect password. Try again.")
    new = input("Enter the password: ")

print("Access Granted")