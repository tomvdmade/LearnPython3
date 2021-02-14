# from the module named sys, import argv (argument vector > parameters). 
# argv  is a list containing all the command line arguments passed into the python script you're currently running. (run in the command line vs input)
from sys import argv
# define argv 0 and 1 as script and filename respectively
script, filename = argv

# create a variable called txt and assign it the file object open returns
txt = open(filename)

#
print(f"Here's youre file {filename}:")
# print the context of the returned file in line 8
print(txt.read())

txt.close()

# print text
print("Type that filename again:")
# declare a variable named file_again to user input
file_again = input("> ")

# create a variable called txt and assign it the file object open returns
txt_again = open(file_again)

# print the context of the returned file assigned to txt_again
print(txt_again.read())

txt_again.close()