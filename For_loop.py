"""
i = 1
while i <= 10:
    print(i)
    i +=1


rows = 6

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end= " ")
    
    print('')




i = 1
new = int(input("Enter the digit : "))
sum = 0
while i <= new :
    sum = sum + i
    i += 1
print("Sum is : ", sum)

rows = 6

for i in range (1,rows + 1):
    for j in range (1,i+1):
        print(j, end=" ")
    print(' ')


data = int(input("Enter the value : "))
i = 1
while data >= i:
    print("The table of given number is ",data , "*",i,"=",data*i )
    i += 1
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
index = 0
max = numbers[0]
while index < len(numbers):
    if(max % 5 ==0):
        print(numbers)
    index += 1
