#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines=0
school_file=open('school_prompt.txt','r')
for i in school_file:
    num_lines=num_lines+1
print(num_lines)
