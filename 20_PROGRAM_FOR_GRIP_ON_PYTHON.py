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
"""
#Take a word from the user and print it in reverse.
name = input("Enter the word : ")
reversed_name = name[ :: -1 ]
print("The reverse list is : ",reversed_name)
"""
#Print only numbers greater than 10.
numbers = [4, 7, 12, 3, 9, 20]
index = 0

while index < len(numbers):
    if numbers[index] > 10:
        print(numbers[index])
    index += 1  
