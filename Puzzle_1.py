
# Write a program to solve a puzzle:

# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?


### SURU KARO QUESTION SOLVE KRNA LEKE PRABHU KA NAAM..

head=35
leg=94
number_of_rabbit=(leg-2*head)/2
if(number_of_rabbit==int(number_of_rabbit)):
    number_of_chicken = (4 * head - leg) / 2
    print(f"You have {int(number_of_chicken)} chickens and {int(number_of_rabbit)} rabbits.")

else:
    print("Sorry from the given heads and legs we are not able to calculate....Solution not possible")






