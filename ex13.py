from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
first = input("Your first variable is: ")
second = input("Your second variable is: ")
# third = input("Your third variable is: ")

print(first + " " + second )