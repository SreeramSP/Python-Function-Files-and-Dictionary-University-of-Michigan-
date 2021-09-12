#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words

num_words=0
emotion_file=open('emotion_words.txt','r')
for i in emotion_file:
    num_words=num_words+len(i.split(" "))
print(num_words)

