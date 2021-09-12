# Create a list called emotions that contains the first word of every line in emotion_words.txt.

emotions=[]
emotions_file=open('emotion_words.txt','r')
for i in emotions_file:
    emotions.append(i.split()[0])
print(emotions)
