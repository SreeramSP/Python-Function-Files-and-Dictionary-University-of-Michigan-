#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(l):
    i=0
    for j in l:
        i=i+j
    return i
list1=[1,2,3,4,5]
print(accum(list1))
