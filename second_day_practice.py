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
"""
sentence = "i am a good boy and do everything wisely"
print(sentence.replace("good", "bad"))
#Question 6

ver_name = str(input ("Enter the name : "))
print("The name is :", ver_name)
if(len(ver_name) >= 10):
 print( "Long words")

elif(len(ver_name) >=5 and len(ver_name) <=10 ):
 print ("Medium words")

else:
 print("Small words")

# Level 3 — Intermediate
# Question 7
First_sentence = "Hi my name is abdulrehman and i am a student of software engineering"

print("The first five character are: ", First_sentence[0 : 6])
    """

# Question 8
we_name = str(input ("Enter the name : "))

if(we_name [0] == "A" or  we_name [0] == "a"):
    print("Sentence starts With A or a")
else:
     print("Sentence doesnot starts With A or a")