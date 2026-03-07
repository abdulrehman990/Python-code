"""
Level 1 — Basic (Warm-up)
Question 1
Take a string from the user and print:
Length of the string
First character
Last character """
"""
Name =  input("Enter the name: ")

print("My name is :" , Name)
print("The lenght of the name is :", len(Name))

# Question 2 : Take a name from the user and convert the first letter into capital. 
Name =  "abdul rehman"
print( Name.capitalize ())

# Question 3: Take a sentence from the user and count how many times "a" appears.
sub = "Pakistan is amazing"
print(sub.count("a")) 

# Level 2 — Beginner Logic
#Question 4: Take a word from the user and check: If the word ends with "ing" → print "Verb" Otherwise → print "Not a verb" 


verb_name = input ("Enter the name : ")

if(verb_name.endswith("ing")):
    print("its a verb")

else:
    print("Not a verb")

    """

# Question no 5: Take a sentence and replace the word "bad" with "good".

sentence = "i am a good boy and do everything wisely"
print(sentence.replace("good", "bad"))