#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
travel_file=open('travel_plans.txt','r')
num=0
for i in travel_file:
    num=num+len(i)
print(num)