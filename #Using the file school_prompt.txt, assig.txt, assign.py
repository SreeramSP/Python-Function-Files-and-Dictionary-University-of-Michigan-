#Using the file school_prompt.txt, assign the third word of every line to a list called three.

school_file=open('school_prompt.txt','r')
three=[]
for i in school_file:
    three.append(i.split()[2])
print(three)
