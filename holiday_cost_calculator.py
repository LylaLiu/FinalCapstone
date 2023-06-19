#input the city, hotel nights and rental days and use try-except block to check the input type
while True:
    print("Your holiday plan: 1.London\t2.Phuket\t3.Hongkong\t4.Agadir")
    try:
        city_flight = int(input("Please enter the number of your destination:"))
        num_nights = int(input("Please enter the number of nights you will stay at a hotel: "))
        rental_days =int(input("Please enter the number of days that you will hire a car for: "))
    except ValueError:
        print("\nPlease enter the correct number.\n")
        continue
    
    #check the value of city_flight 
    if city_flight not in range(1,5):
        print("\nPlease enter the correct number for the city name.\n")
        continue
    else:
        break
    
#caculate the plane cost. 1 stands for London, 2 stands for Phuket, 3 stands for Hongkong and 4 stands for Agadir.
plane_city = {1:50, 2:60,  3:70, 4:80}
if city_flight in plane_city:
    plane_cost = plane_city[city_flight]
    print("Your plane cost is: " + str(plane_cost))

#caculate the hotel cost, 100 for each night
def hotel_cost(num_nights):
    return num_nights * 100
hotel_fee = hotel_cost(num_nights)
print("Your hotel cost is: " + str(hotel_fee))

#caculate the car rental fee, 30 for each day
def car_rantal(rental_days):
    return rental_days * 30
rental_fee = car_rantal(rental_days)
print("Your car rantal cost is: " + str(rental_fee))

#caculate holiday total cost
def holiday_cost():
    return hotel_fee + rental_fee + plane_cost

print("Your holiday total cost is: " + str(holiday_cost()))