previous_meter = int(input("What was your previous meter reading: "))
current_meter = int(input("What was your current meter reading: "))
unit_cost = int(input("What was is your unit cost: "))
discount = input('Are you eligible for a discount: ')
cost = ((current_meter - previous_meter) * unit_cost)
while current_meter < previous_meter:
    print("Error, please give an accepted current meter value ")
    current_meter = int(input("What was your current meter reading: "))
else:
    if discount == 'yes':
        cost -= 5
    print('£',cost)


