#Talent Show
#Supreme Neupane
#25/06/24


name = str(input("What is your name?"))
age = int(input("What is your age?"))
while age < 11 or age > 18:
    print("Invalid age")
    age = int(input("What is your age?"))
print("Welcome to the talent show,", name)
