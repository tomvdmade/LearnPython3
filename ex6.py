types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# string inside string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# string inside string
print(f"I said: {x}")
# string inside string
print(f"I also said: '{y}'")

hilarious = False
joke_evalution = "Isn't that joke so funny?! {}"

# string inside string
print(joke_evalution.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
