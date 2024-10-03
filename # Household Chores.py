# Household Chores
# Supreme Neupane
# 27/09/24

number = int(input("Input the number 1, 2, 3  or 4:"))
while number < 0 or number >5 or number == 5:
    print("Error, number must be between 1 and 4")
    number = int(input("Input the number 1, 2, 3  or 4:"))
if number == 1:
    print("View chores")
elif number == 2:
    print("Mark chores as completed")
elif number == 3:
    print("View completed chores")
else:
    print("Exit")