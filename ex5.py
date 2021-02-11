name = 'Tom van der Made'
age = 30 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Grey/Green'
teeth = 'White'
hair = 'Dark Blonde'

height_cm = round(height * 2.54)
weight_kg = round(weight * 0.453592)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are ussually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"Using the metric system, {name} would be {height_cm} centimeters tall and {weight_kg} kilo's heavy.")