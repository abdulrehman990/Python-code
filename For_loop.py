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



"""

i = 1
new = int(input("Enter the digit : "))
sum = 0
while i <= new :
    sum = sum + i
    i += 1
print("Sum is : ", sum)