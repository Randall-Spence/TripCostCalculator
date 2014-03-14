#Function defining total hotel expense.
def hotel_cost(nights):
    return 140 * nights
 
#Function defining total flight expense.
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183  
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222 
    elif city == "Los Angeles":
        return 475
  
#Function defining total rental car expense.
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
    
#Function defining total trip expense.
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

#Displays results based on input.
print trip_cost("Los Angeles", 5, 600)