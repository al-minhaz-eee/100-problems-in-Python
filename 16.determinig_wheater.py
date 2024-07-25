"""
 16. Write a program that will determine weather when the value of
 temperature and humidity is provided by the user.
 TEMPERATURE(C) HUMIDITY(%) WEATHER
 >= 30 >=90 Hot and Humid
 >= 30 < 90 Hot
 <30  >= 90  Cool and Humid
 <30 <90  Cool
"""
temparature  = float(input("Enter the value of temperature in Celcius: "))
humidity = float(input("Enter the value of humidity(%): "))

if temparature >= 30 and humidity >=90:
    print("Hot and Humid")
elif temparature >= 30 and humidity < 90:
    print("Hot")
elif  temparature <30  and humidity>= 90:
    print("Cool and Humid")
else:
    print("Cool")