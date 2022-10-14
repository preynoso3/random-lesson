from random import randint
from random import shuffle
from random import choice
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
# print("random")
# dice1 = randint(1,6)
# print(f"dice1 : {dice1}")
# dice2 = randint(1,6)
# print(f"dice2 : {dice2}")
# rolledDoubles = dice1 == dice2
# if rolledDoubles:
#   print("you rolled doubles")
# else:print("you did not roll doubles")

# # create a way to roll snakes
# if dice1 ==1 and dice2 == 1:
#   print("you rolled snake eyes")
# else: print("you did not roll snake eyes")

# practice with shuffle

my_list = range(1,51)
print("My new list")
print(list(my_list))
my_list = list(my_list)
shuffle(my_list)
print(my_list)

# challenge
new_list = randint(1, 200)
print("New list")
print(new_list)
if new_list%2 == 0:
  print("It is even")
else:
  print("It is odd")

color = ["red", "blue", "pink", "purple"]
random_color = choice(color)
print(f"random color is {random_color}")