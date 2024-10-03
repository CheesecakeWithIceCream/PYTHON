lotterynumbers = []

for loop in range(6):
    number = int(input("Enter lottery number:"))
    while (number < 1) or (number > 49):
        print("Number must be between 1 and 49")
        number = int(input("Enter lottery number:"))

lotterynumbers.append(number)

print("your lottery numbers are:,",  lotterynumbers)
