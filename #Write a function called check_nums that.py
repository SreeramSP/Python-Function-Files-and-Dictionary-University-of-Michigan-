#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


def check_nums(i):
    s1=[]
    i=(item for item in i)
    item=next(i,5)
    while item != 7:
        s1.append(item)
        item=next(i,7)
    return s1
x=[1,2,3,4,5,6,7,8,9]
check_nums(x)

