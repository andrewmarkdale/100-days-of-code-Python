"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day: 
2

Project: 
Tip Calculator

Purpose:
To calculate what each person owes after adding a percentage tip.

Example:
If the bill for the service was $10.00, we wanted to add a 10% tip and there were 2
people splitting the bill the output would be "Each person should pay $5.50 
"""

print("Welcome to the tip calculator.")
bill_total = float(input("What was the bill total? $"))
tip_percentage = int(input("Would you like to tip 10, 12 or 15%? "))
total_patrons = int(input("How many people are going to split the bill? "))
per_patron = round(((bill_total + bill_total*(tip_percentage/100))/total_patrons), 2)
print("Each person should pay ${:.2f}".format(per_patron))
