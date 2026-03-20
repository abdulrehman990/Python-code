"""
#Program no 1
cities = ["faisalabad","lahore","islamabad","rawalpindi","karachi"]

def print_len(lists):
    print(len(lists))

print_len(cities)

#program no 2
cities = {"faisalabad","lahore","islamabad","rawalpindi","karachi"}

def print_list(lists):
    print(lists)

print_list(cities)

#program no 3
cities = {"faisalabad","lahore","islamabad","rawalpindi","karachi"}

def print_list(lists):
    for list in cities:
        print(list, end=" ")

print_list(cities)

#program no 4
def factorial(n):
    for i in range(1,n+1):
        n *= i
        print(n)

factorial(7)

#program no 5
def currency(n):
    pakistani_rupees = n * 280
    print("Price of", n , "Dollars in pakistani rupees is : ", pakistani_rupees)

currency(2)
"""
#program no 5
def check_number(number):
    number = input("Enter the number : ")
    if (number % 2 == 0):
        print("Even number : ")
    else:
        print("Odd number : ")
check_number(number=input())
