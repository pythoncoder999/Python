# Create the superclass
class Monster(object):

# Set up the class attribute, the same for all instances
	eats = 'food'

# Define the __init__method
	def __init__(self, name):

# Set up an instance attribute, different for each intance
		self.name = name

# Define a method for speaking behavior
	def speak(self):
		print(self.name + ' speaks')

# Define a method for eating behavior
	def eat(self, meal):
		if meal == self.eats:
			print("yum!")
		else:
			print("blech!")
	

# Create an instance of MonsterFood
# my_monster = Monster("Spooky Snack")

# Call the methods on the new instance
# my_monster.speak()
# my_monster.eat('food')

# Create a subclass of Monster
class FrankenBurger(Monster):

# Set up a clss attribute
	eats = 'hamburger patties'

# Define any methods that are different from the superclass
	def speak(self):
		print('My name is ' + self.name + 'Burger')
		
# Create an intance of FrankenBurger
# Pass in the name 'Veggiesaurus'
# my_frankenburger = FrankenBurger('Veggiesaurus')

# Call the speak method
# my_frankenburger.speak()

# Call the eat method. Pass in 'pickles'
# my_frankenburger.eat('pickles')

class CrummyMummy(Monster):
	eats = 'chocolate chips'
	def speak(self):
		print('My name is ' + self.name + 'Mummy')


class WereWatermelon(Monster):
	eats = 'watermelon juice'
	def speak(self):
		print('My name is Were' + self.name)
		
monster_selection = input('What kind of monster do you want to create? Select: frankenburger, crummymummy, or werewatermelon.')

monster_name = input('What do you want to name your monster?')
monster_meal = input('What will you feed your monster?')
# To Do: Add monster_meal here

if monster_selection == 'frankenburger':
	monster_type = FrankenBurger
elif monster_selection == 'crummymummy':
	monster_type = CrummyMummy
	
# To Do: Test for the selection 'werewatermelon'
# To Do: Assign the type WereWatermelon
else:
	monster_type = Monster

my_monster = monster_type(monster_name)

# To Do: Call the speak method
my_monster.speak()

# To Do: Call the eat method
my_monster.eat(monster_meal)