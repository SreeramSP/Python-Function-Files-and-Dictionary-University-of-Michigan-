#Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
words=sent.split()
for i in words:
    if i not in wrd_d:
        wrd_d[i]=1
    else:
        wrd_d[i]+=1
print(wrd_d)
