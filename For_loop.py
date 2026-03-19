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


#for all numbers sum

i = 1
new = int(input("Enter the digit : "))
sum = 0
while i <= new :
    sum = sum + i
    i += 1
print("Sum is : ", sum)

#for 1 12 123 1234 12345
rows = 6

for i in range (1,rows + 1):
    for j in range (1,i+1):
        print(j, end=" ")
    print(' ')

#table
data = int(input("Enter the value : "))
i = 1
while data >= i:
    print("The table of given number is ",data , "*",i,"=",data*i )
    i += 1

#for find divide by 5
numbers = [12, 75, 150, 180, 145, 525, 50]

index = 0

while index < len(numbers):
    if numbers[index] % 5 == 0:
        print(numbers[index])
    index += 1

#for max number
numbers = [12, 75, 150, 180, 145, 525, 50]

index = 0
max = numbers[0]

while index < len(numbers):
    if max < numbers[index]:
        max = numbers[index]
    index += 1
print(max)

words = int(input("Enter the digits : "))
count = 0

while words != 0:
    words = words // 10   # last digit remove
    count += 1

print("Total numbers:", count)


sums = 6
for i in range(sums-1,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print('')
"""

for i in range(0,6):
    for j in range(i,i+2,2):
        print("       *       ",end=" ")
    print(i)
