
#Write a Python program to get a string made of the first 2 and the last
#2 chars from a given a string. If the string length is less than 2, return
#instead of the empty string.

n=input("enter string: ")

if len(n)<2:
    n=""
    print(n)
else:
    print(n[:2]+n[-2:])
    
