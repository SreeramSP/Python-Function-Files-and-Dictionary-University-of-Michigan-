#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(l):
    if len(l)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'
list1=[1,2,3,4,5]
print(length(list1))
