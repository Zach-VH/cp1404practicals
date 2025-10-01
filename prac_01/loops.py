#Example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a. count in 10's
for i in range(0,110,10):
    print(i, end=' ')
print()

#b. counting downwards
for i in range(20,0,-1):
    print(i, end=' ')
print()

#c. Printing as many stars as user specifies
number_of_stars = int(input("Enter amount of stars: "))
for i in range(0,number_of_stars,1):
    print("* ",end='')
print()

#d. Printing lines of stars
n = ""
number_of_lines = int(input("Enter number of lines of stars: "))
for i in range(0,number_of_lines,1):
    n = n + "* "
    print(n,end="\n")
print()