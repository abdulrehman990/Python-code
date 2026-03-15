#Print numbers 1 to 100, but print only numbers divisible by 3.
"""
i= 1
while i <= 100:

    if i % 3 == 0:  
        print(i)
    i += 1
"""
"""
#Take a number from the user and count how many digits it has.
data = input("Enter the word : ")
print("The given word is : ",data)
print("The character in given word is : ",len(data))
"""
student = ["name","digit" ,"word"]

index = 0 
count= 0
data = input("Enter the word : ")
while index < len(student):
    if data == student[index]:
        print("DATA IS IN IT ")

    index += 1

count +=1
print("The count is :",count)
