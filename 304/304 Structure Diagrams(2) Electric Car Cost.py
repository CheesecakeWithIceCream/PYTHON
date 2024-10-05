# Program: Electric Car Cost
# 06/09/24
num_charging_stations = 3
start_miles = 0
for index in range(num_charging_stations):
    current_miles = int(input("What is your your current mileage:"))
    kw_rating = int(input("What is the kW rating:"))
    if kw_rating == 7:
        price_per_mile = 0
    elif kw_rating == 22:
        price_per_mile = 0.005
    else:
        price_per_mile = 0.01
    miles_travelled = (current_miles - start_miles)
    start_miles = current_miles
    cost_of_journey_stage = price_per_mile * miles_travelled



