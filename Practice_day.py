
Name = "Hi My name is Abdul rehman"
print(Name)
password = input("Enter the password: ")

if not password.isalnum():
    print("Password contains special characters")

elif password.isdigit():
    print("Good one but require special character for strong one")

elif password.isalpha():
    print("Good one but require more ")

elif password.isalnum(): 
    print("Good enogh but require more")  

else:
    print("Error")
