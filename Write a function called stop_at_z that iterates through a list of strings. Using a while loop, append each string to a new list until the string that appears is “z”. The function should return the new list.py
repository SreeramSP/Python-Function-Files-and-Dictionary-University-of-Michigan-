#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

def stop_at_z(l):
    i=0
    while(i<len(l)):
        if(l[i]=='z'):
            return l[0:i]
        i=i+1
    return False

