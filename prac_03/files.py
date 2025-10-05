"""
CP1404 - Practice
Various exercise for file reading and writing
"""

# Exercise 1: Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
print("Starting Exercise 1")
name = input("Enter your name: ")
out_file = open('name.txt','w')
print(name,file=out_file)
out_file.close()
print("Finished")

# Exercise 2: In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name
# then prints "Hi name!"
print("Starting Exercise 2")
in_file = open('name.txt','r')
name_from_file = in_file.readline()
print(f"Hi {name_from_file.strip()}!")
in_file.close()
print("Finished")

# Exercise 3: Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result
print("Starting Exercise 3")
with open('numbers.txt','r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)
print("Finished")

# Exercise 4:Now write a fourth block of code that prints the total for all lines in numbers.txt.
# This should work for a file with any number of numbers.
print("Starting Exercise 4")
with open('numbers.txt','r') as in_file:
    lines = in_file.readlines()
    number_of_lines = len(lines)
    print(number_of_lines)
    print("Finished")
