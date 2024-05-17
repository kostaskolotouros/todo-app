import random

lower_bound_input = int(input("Enter the lower bound: "))
upper_bound_input = int(input("Enter the upper bound: "))

random_integer = random.randint(lower_bound_input, upper_bound_input)
print(random_integer)