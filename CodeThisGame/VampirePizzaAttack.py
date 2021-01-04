#import libraries
import pygame
from pygame import *
from random import randint

#initializa pygame
pygame.init()

# Set up clock
clock = time.Clock()

#Define constant variables

#To Do: Create a variable for the window width here
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Define tile parameters
WIDTH = 100
# To Do: Add HEIGHT here
HEIGHT = 100

# Define colors
WHITE = (255,255,255)

# To Do: Define SPAWN_RATE
SPAWN_RATE = 360
FRAME_RATE = 60

# Store the number of pizza bucks that players get at 
# the start of the game
STARTING_BUCKS = 15
# To Do: Add BUCK_RATE here
BUCK_RATE = 120
# To Do: Add STARTING_BUCK_BOOSTER here
STARTING_BUCK_BOOSTER = 1

# Set up win/lose conditions
MAX_BAD_REVIEWS = 3
WIN_TIME = FRAME_RATE * 60 * 3

# Define speeds
REG_SPEED = 2

# To Do: Add the variable for slow speed here
SLOW_SPEED = 1
# ---
# Load assets

#To Do: Create a variable for the window height here
#To Do: Create a variable for window resolution here

#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)

#To Do: Add window caption here
display.set_caption("Attack of the Vampire Pizza!")

#To Do: Add background_img
background_img = image.load('restaurant.jpg')

# To Do: Add background_surf
background_surf = Surface.convert_alpha(background_img)

# To Do: Add BACKGROUND
BACKGROUND = transform.scale(background_surf, WINDOW_RES)  

#Set up the enemy image
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf,(WIDTH,HEIGHT))

# Set up trap images
garlic_img = image.load('garlic.png')
garlic_surf = Surface.convert_alpha(pizza_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))

# To Do: Load pizza cutter image
cutter_img = image.load('pizzacutter.png')

# To Do: Convert pizza cutter to a surface
cutter_surf = Surface.convert_alpha(cutter_img)

# To Do: Set the size of the pizza cutter
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))

# To Do: Use 3 lines of code to import and set up the 
# pepperoni image
pepperoni_img = image.load('pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))


# ---
# Set up classes

# Create a subclass of Sprite called VampireState
class VampireSprite(sprite.Sprite):

# Define the VampireSprite set-umethod
	def __init__(self):
# Take all the behavior rules from the Sprite class and use
# them for VampireSprite
		super().__init__()
# Set the default movement speed
		# self.speed = 2
		self.speed = REG_SPEED
# Randomly select a lane between o and 4
		self.lane = randint(0,4)
# Add all vampire pizza sprites to a group called all_vampires
		all_vampires.add(self)
# Use the VAMPIRE_PIZZA image as the image for
# vampire pizza sprites.copy()
		self.image = VAMPIRE_PIZZA.copy()
# Set each sprite's y-coordinate at the middle of the
# selected lane
		y = 50 + self.lane * 100
# Create a rect for each sprite and place it just off the
# right side of the screen in the correct lane
		self.rect = self.image.get_rect(center = (1100,y))

# To Do: Create an attribute called health here
		self.health = 100
# To Do: Add update method here
	# def update(self, game_window):
	def update(self, game_window, counters):

# To Do: Blit the vampire pizza image here
		# game_window.blit(self.image, (self.rect.x, self.rect.y))
		game_window.blit(BACKGROUND,(self.rect.x, self.rect.y), self.rect)
		self.rect.x -= self.speed
		if self.health <= 0 or self.rect.x <= 100:
			self.kill()
			if self.rect.x <= 100:
				counter.bad_reviews += 1
		else:
			game_window.blit(self.image, (self.rect.x, self.rect.y))
# To Do: Set rect attribute here
	def attack(self, tile):
		if tile.trap == SLOW:
			self.speed = SLOW_SPEED
# To Do: Test for the DAMAGE trap here
		if tile.trap == DAMAGE:
			self.health -= 1

# Create new class
class Counters(object):
# Set up init method with four arguments
	# def __init__(self, pizza_bucks, buck_rate, buck_booster):
	def __init__(self, pizza_bucks, buck_rate, buck_booster, timer):
# Start the game loop counter at 0
		self.loop_count = 0
# Set up the look of the counter on the screen
		self.display_font = font.Font('pizza_font.ttf',25)
# Define the pizza_bucks attribute using the pizza_bucks
# argument
		self.pizza_bucks = pizza_bucks
# Define the buck_rate attribute using the buck_ratargument
		self.buck_rate = buck_rate
# To Do: Define the buck_booster attribute
		self.buck_booster = buck_booster
# To Do: Define the bucks_rect attribute
		self.bucks_rect = None
		self.timer = timer
		self.timer_rect = None
		
# To Do: Add bad_reviews attribute here
		self.bad_reviews = 0
# To Do: Add bad_reviews_rect attribute here
		self.bad_reviews_rect = None
# Increase the player's pizza buck based on time passing
	def increment_bucks(self):
# Add a set number of pizza bucks to the player's total once
# every 120 times the game loop runs(approx.every 2 seconds)
		if self.loop_count % self.buck_rate == 0:
			self.pizza_bucks += self.buck_booster
# Define a new method with two arguments
	def draw_bucks(self, game_window):
# Erase the last number from the game window
		if bool(self.bucks_rect):
			game_window.blit(BACKGROUND,(self.bucks_rect.x,self.bucks_rect.y),self.bucks_rect)
		bucks_surf = self.display_font.render(str(self.pizza_bucks),True,WHITE)
# Create a rect for bucks_surf
		self.bucks_rect = bucks_surf.get_rect()
# Place the counter in the middle of the tile on the
# bottom-right corner
		self.bucks_rect.x = WINDOW_WIDTH - 150
		self.bucks_rect.y = WINDOW_HEIGHT - 50
# Display the new pizza bucks total to the game window
		game_window.blit(bucks_surf, self.bucks_rect)
		
		
# Draw the player's bad reviews total to the screen
	def draw_bad_reviews(self, game_window):
# Test if there is a new number of bad reviews and erase the
# old number if there is
		if bool(self.bad_rev_rect):
			game_window.blit(BACKGROUND, (self.bad_rev_rect.x, self.bad_rev_rect.y), self.bad_rev_rect)
# Tell the program the font and color to use in the display
		bad_rev_surf = self.display_font.render(str(self.bad_reviews), True, WHITE)
# Set up a rect so that we can interact with the number
		self.bad_rev_rect = bad_rev_surf.get_rect()
# Put the display in the second-to-last column and bottom
# row of the grid
		self.bad_rev_rect.x = WINDOW_WIDTH - 150
		self.bad_rev_rect.y = WINDOW_HEIGHT - 50
# Display the number to the screen
		game_window.blit(bad_rev_surf, self.bad_rev_rect)
		
# To Do: Define the method draw_time here
	def draw_timer(self, game_window):
# To Do: Test for a new time
		if bool(self.timer_rect):
# To Do: Erase the old time if there's a new one
			game_window.blit(BACKGROUND, (self.timer_rect.x, self.timer_rect.y), self.timer_rect)
		
# To Do: Tell the program the font and color for the display
		timer_surf = self.display_font.render(str((WIN_TIME - self.loop_count)//FRAME_RATE), True, WHITE)
# To Do: Set up rect
		self.timer_rect = timer_surf.get_rect()

# To Do: Tell the program which column to put the display in
		self.timer_rect.x = WINDOW_WIDTH - 250
# To Do: Tell the program which row to put the display in
		self.timer_rect.y = WINDOW_WIDTH - 50
# To Do: Display the time to the screen
		game_window.blit(timer_surf, self.timer_rect)
		
# To Do: Define a method called update here
	# def update(self):
	def update(self, game_window):
# To Do: Add 1 to the value of loop_count here
		self.loop_count += 1
# To Do: Call the increment_bucks method here
		self.increment_bucks()
		
# To Do: Call the draw_bucks method here
		self.draw_bucks(game_window)
		self.draw_bad_reviews(game_window)
		
# To Do: Call the draw_timer method here
		self.draw_timer(game_window)
# Set up the different kinds of traps
class Trap(object):
	def __init__(self, trap_kind, cost, trap_img):
		self.trap_kind = trap_kind
		self.cost = cost
		self.trap_img = trap_img
		
# To Do: Create a class called TrapApplicator here
class TrapApplicator(object):

# To Do: Define an __init__ method here
	def __init__(self):
# To Do: Add an attribute called selected here
		self.selected = None
# To Do: Define the select_trap method here
	def select_trap(self, trap):
# To Do: Test if cost less than or equal to pizza bucks
		if trap.cost <= counters.pizza_bucks:
			self.selected = trap
				
	def select_tile(self, tile, counters):
		self.selected = tile.set_trap(self.selected, counters)
# To Do: If it is, change the value of the self.selected


# To Do: Create BackgroundTile clas here
class BackgroundTile(sprite.Sprite):

# To Do: Define init methohere
	def __init__(self, rect):

# To Do: Use super method here
		super().__init__()

# To Do: Set effect attributhere
		# self.effect = False 
		self.trap = None
		self.rect = rect

# A subclass of BackgroundTile where the player can set traps
class PlayTile(BackgroundTile):
# Set the trap on the selected play tile
	def set_trap(self, trap, counters):
		if bool(trap) and not bool(self.trap):
			counters.pizza_bucks -= trap.cost
			self.trap = trap
			if trap == EARN:
				counters.buck_booster += 1
		return None
					
# Draw the trap image to the select play tile
	def draw_trap(self, game_window, trap_applicator):
		if bool(self.trap):
			game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

# To Do: Create the ButtonTile class here
class ButtonTile(BackgroundTile):
# To Do: Define the set_trap method here
	def set_trap(self, trap, counters):
# To Do: Test if the player has enough pizza bucks here
		if counters.pizza_bucks >= self.trap.cost:
# To Do: If player has enough pizza bucks, return self.trap
			return self.trap
# To Do: Else
		else:
# To Do: Return trap
			return None
# To Do: Define the draw_trap method here
	def draw_trap(self, game_window, trap_applicator):
# To Do: Test if selected is True and if selected is equal
# to self.trap
		if bool (trap_applicator.selected):
			if trap_applicator.selected == self.trap:
# To Do: If the test is True, draw a rectangle on the 
# selected button tile
				draw.rect(game_window, (238, 190, 47), (self.rect.x, self.rect.y, WIDTH, HEIGHT),5)
# To Do: Create the InactiveTile class here
class InactiveTile(BackgroundTile):
# To Do: Define the set_trap method here
	def set_trap(self, trap, counters):
	
# To Do: Return trap
		return None
# To Do: Define the draw_trap method here
	def draw_trap(self, game_window, trap_applicator):
# To Do: Pass
		pass

# ---
# Create class instances and groups
# Create a group for all the VampireSprite instances
all_vampires = sprite.Group()

counters = Counters(STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER, WIN_TIME)

SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)

# To Do: Add EARN trap here
EARN = Trap('EARN', 7, PEPPERONI)
# ---
# To Do: Create TrapApplicator instance here
trap_applicator = TrapApplicator()

# ---
# Initialize and draw background grid
# Create an empty list
tile_grid = []

# To Do: Create tile_color variable here
tile_color = WHITE

for row in range(6):
# Create an empty list each time the loop runs
	row_of_tiles = []
# Add each of the six lists called row_of_tiles to the
# tile_grid list above
	tile_grid.append(row_of_tiles)

# Notice this method is broken up into two lines
	for column in range(11):
# Create an invisible rect for each background tile sprite 
		tile_rect = Rect(WIDTH*column, HEIGHT*row,
						WIDTH, HEIGHT)
# For each column in each row, create a new background tilsprite
		# new_tile = BackgroundTile(tile_rect)
		
		if column <= 1:
			new_tile = InactiveTile(tile_rect)
		else:
			if row == 5:
				if 2<= column <= 4:
					new_tile = ButtonTile(tile_rect)
					new_tile.trap = [SLOW, DAMAGE, EARN][column-2]
				else:
					new_tile = InactiveTile(tile_rect)
			else:
				new_tile = PlayTile(tile_rect)
# Add each new background tile sprite to the correct
# row_of_tiles list
		row_of_tiles.append(new_tile)
		if row == 5 and 2<= column <= 4:
			BACKGROUND.blit(new_tile.trap.trap_img, (new_tile.rect.x, new_tile.rect.y))
		# draw.rect(BACKGROUND, tile_color, 
				# (WIDTH*column, HEIGHT*row, WIDTH, HEIGHT), 1)
		if column != 0 and row != 5:
			if column != 1:
				draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)
				
# To Do: Blit BACKGROUND at (0,0)
GAME_WINDOW.blit(BACKGROUND, (0,0))

# Display the enemy image to the screen
# GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))

#Add a giant pepperoni
# draw.circle(GAME_WINDOW, (255,0,0),(925,425),25,0)

#Put it in a pizza box
# draw.rect(GAME_WINDOW, (160,82,45), (895,395,110,110),5)

#Give it a lid
# draw.rect(GAME_WINDOW, (160,82,45),(895,295,110,110),0)
#------
#Start Main Game Loop
game_running = True
program_running = True
#Game Loop
while game_running:

#Check for events
	for event in pygame.event.get():

#Exit loop on quit
		if event.type == QUIT:
			# game_running = False
			game_running = False
			program_running = False
# Listen for the mouse button to be clicked and run when clicked
		elif event.type == MOUSEBUTTONDOWN:
			
# Get the (x,y) coordinate where the mouse was clicked
# on the screen
			coordinates = mouse.get_pos()
			x = coordinates[0]
			y = coordinates[1]
			
# Find the background tile at the location where the mouse
# was cliked and change the value of effect to True
			tile_y = y // 100
			tile_x = x // 100
			# tile_grid[tile_y][tile_x].effect = True
			# print(x,y)
			trap_applicator.select_tile(tile_grid[tile_y][tile_x], counters)
			
# To Do: Add second print statement here
			# print("You clicked me!")
# spawn vampire pizza sprites
	if randint(1,SPAWN_RATE) == 1:
		VampireSprite()
		
	for tile_row in tile_grid:
		for tile in tile_row:
			if bool(tile.trap):
				GAME_WINDOW.blit(BACKGROUND, (tile.rect.x, tile.rect.y), tile.rect)
		
# ---
# set up collision detection
# Run through each vampire pizza sprite in the
# list all_vampires
	for vampire in all_vampires:
# store the row where the vampire sprite is located
		tile_row = tile_grid[vampire.rect.y//100]
# store the current location of the left edge of the
# vampire spirite
		vamp_left_side = vampire.rect.x //100
		
# Store the current location of the right edge of the
# vampire sprite
		vamp_right_side = (vampire.rect.x +
							vampire.rect.width)//100

# If the vampire sprite is on the grid, find which column
# it is in
		if 0<= vamp_left_side <=10:
			left_tile = tile_row[vamp_left_side]
			
# Return no column if the vampire sprite is not on the grid
		else:
			left_tile = None
		if 0<= vamp_right_side <=10:
			right_tile = tile_row[vamp_right_side]
		else:
			right_tile = None
		
		if bool(left_tile):
			vampire.attack(left_tile)
		if bool(right_tile):
			if right_tile != left_tile:
				vampire.attack(right_tile)

# To Do: Test for the lose condition here
	if counters.bad_reviews >= MAX_BAD_REVIEWS:
# To Do: If the player lost set game_running to False
		game_running = False
# To Do: Test for the win condition here
	if counters.loop_count > WIN_TIME:
# To Do: If the player won set game_running to False
		game_running = False
# Update displays
	for vampire in all_vampires:
		# vampire.update(GAME_WINDOW)
		vampire.update(GAME_WINDOW, counters)
		
	for tile_row in tile_grid:
		for tile in tile_row:
			tile.draw_trap(GAME_WINDOW, trap_applicator)
# To Do: Call the Counters update method here
	counters.update(GAME_WINDOW)
	display.update()

# To Do: Set the frame rate
	clock.tick(FRAME_RATE)

# Set up the font
end_font = font.Font('pizza_font.ttf', 50)

# Test if either the win or lose condition has been met
if program_running:
# To Do: Test for lose condition here
	if counters.bad_reviews >= MAX_BAD_REVIEWS:
# To Do: Render the lose message here(end_surf, (350,200))
		end_surf = end_font.render('Game Over', True, WHITE)
# To Do: Else
	else:
# To Do: Render the win message here
		end_surf = end_font.render('You Win', True, WHITE)
# To Do: Blit the end message to the screen
	GAME_WINDOW.blit(end_surf,(350, 200))
	display.update()

# Start end-of-game
while program_running:
	for event in pygame.event.get():
# Listen for the QUIT event
		if event.type == QUIT:
			program_running = False
# Set the frame rate
	clock.tick(FRAME_RATE)


#End of main game loop
#----
#Clean up game
pygame.quit()
