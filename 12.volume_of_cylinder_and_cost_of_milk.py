"""
 12. Write a program to find the volume of the cylinder. Also find the
 cost when the cost of 1litre milk is 40Rs.
"""
import math

height = float(input("Enter height of cylinder: "))
radius = float(input("Enter base radius of the cylinder: "))

Volume = 2*math.pi*radius*height

cost_of_milk = Volume* 40

print(f"The Volume is {round(Volume, 2)} cupic meter and cost of milk in this volume is {round(cost_of_milk, 2)} Rs")
