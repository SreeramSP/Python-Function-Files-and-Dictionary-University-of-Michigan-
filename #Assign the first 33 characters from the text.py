#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

travel=open("travel_plans.txt","r")
first_chars=travel.read(33)
print(first_chars)

