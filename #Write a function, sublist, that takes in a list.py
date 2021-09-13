#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(i):
    s1=[]
    i=(item for item in i)
    item=next(i,5)
    while item != 5:
        s1.append(item)
        item=next(i,5)
    return s1
x=[1,2,3,4,5,6,7,8,9]
sublist(x)
