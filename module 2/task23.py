

#Write a Python function to insert a string in the middle of a string.

a=input("enter first  string: ")
b=input("enter second string: ")

c=len(a) // 2
print(a[0:c]+b+a[c:])
