# Program: Party Cost
# 06/09/24

child_buffet = 2.00
cake=input("Is cake required?")
if cake == 'yes' or 'Yes' or 'YES':
    cake = 15.00
else:
    cake = 0
adults=int(input("How many adults are going?:"))
children=int(input("How many chiildren are going?:"))
diet = []
for i in range(children):
    message=input("What are your dietary requirements")
    requirements=input(message)
    diet.append(requirements)
if adults + children >= 20:
    venue = 50.00
else:
    venue= 0.00
cost =(child_buffet*children)+cake+venue
print(cost)

