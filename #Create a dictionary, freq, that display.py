#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)