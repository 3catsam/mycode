def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0
def rental_car_cost(days):
    price_per_day = 40
    if days >= 7:
        return days*price_per_day-50
    elif days >= 3 and days < 7:
        return days*price_per_day-20
    else:
        return days*price_per_day
def trip_cost(city,days,spending_money):
    return plane_ride_cost(city)+rental_car_cost(days)+hotel_cost(days)+spending_money
city = str(raw_input("Where to go?"))
days = int(raw_input("How long?"))
spending_money = int(raw_input("How much will you spend?"))
if city in("Charlotte","Tampa","Pittsburgh","Los Angeles"):
    print "total money:",trip_cost(city,days,spending_money)
else: 
    print "total money:",trip_cost(city,days,spending_money),"(Sorry, we cannot find plane ride cost)"