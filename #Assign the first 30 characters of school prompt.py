#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

school_file=open('school_prompt.txt','r')
beginning_chars=school_file.read(30)
print(beginning_chars)
