total = 0
for index in range(5):
    grades = int(input("Enter grades from 0-100: " ))
    while grades < 0 or grades > 100:
        print("Error")
        grades = int(input("Enter grades from 0-100" ))
    total = total + grades

print(total)
