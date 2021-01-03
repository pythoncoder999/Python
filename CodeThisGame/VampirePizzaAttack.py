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
# To Do: Add update method here
	def update(self, game_window):

# To Do: Blit the vampire pizza image here
		# game_window.blit(self.image, (self.rect.x, self.rect.y))
		game_window.blit(BACKGROUND,
						(self.rect.x, self.rect.y), self.rect)
# To Do: Set rect attribute here
		

# Move the sprites
		self.rect.x -= self.speed
# Update the sprite image to the new location
		game_window.blit(self.image,
						(self.rect.x,self.rect.y))
# Create new class
class Counters(object):
# Set up init method with four arguments
	def __init__(self, pizza_bucks, buck_rate, buck_booster):
# Start the game loop counter at 0
		self.loop_count = 0
# Set up the look of the counter on the screen
		self.display_font = font.Font('pizza_font.ttf',25)
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
			game_window.blit(BACKGROUND, 
										(
										self.bucks_rect.x,
										self.bucks_rect.y,
										self.bucks_rect
										)
		bucks_surf = self.display_font.render(str(self.pizza_bucks),True,WHITE)
# Create a rect for bucks_surf
		self.bucks_rect = bucks_surf.get_rect()
# Place the counter in the middle of the tile on the
# bottom-right corner
		self.bucks_rect.x = WINDOW_WIDTH - 50
		self.bucks_rect.y = WINDOW_WIDTH - 50
# Display the new pizza bucks total to the game window
		game_window.blit(bucks_surf, self.bucks_rect)
# To Do: Define a method called update here
	def update(self):
# To Do: Add 1 to the value of loop_count here
		self.loop_count += 1
# To Do: Call the increment_bucks method here
# increment_bucks()
# To Do: Create BackgroundTile clas here
class BackgroundTile(sprite.Sprite):

# To Do: Define init methohere
	def __init__(self, rect):

# To Do: Use super method here
		super().__init__()

# To Do: Set effect attributhere
		self.effect = False

						
# ---
# Create class instances and groups
# Create a group for all the VampireSprite instances
all_vampires = sprite.Group()

counters = Counters(STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER)

# ---


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
		new_tile = BackgroundTile(tile_rect)
		
# Add each new background tile sprite to the correct
# row_of_tiles list
		row_of_tiles.append(new_tile)

		draw.rect(BACKGROUND, tile_color, 
				(WIDTH*column, HEIGHT*row, WIDTH, HEIGHT), 1)

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
#Game Loop
while game_running:

#Check for events
	for event in pygame.event.get():

#Exit loop on quit
		if event.type == QUIT:
			# game_running = False
			running = False
			
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
			tile_grid[tile_y][tile_x].effect = True
			# print(x,y)
			
# To Do: Add second print statement here
			# print("You clicked me!")
# spawn vampire pizza sprites
	if randint(1,SPAWN_RATE) == 1:
		VampireSprite()
		
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
		
# Test if the left side of the vampire pizza is touching
# a tile and if that tile has been clicked
# If true, change the vampire speed to 1.
		if bool(left_tile) and left_tile.effect:
			vampire.speed = SLOW_SPEED
# To Do: Replace the value of vampire.speed
# Test if the right side of the sprite is touchinga tile
# and if that tile has been clicked
		if bool(right_tile) and right_tile.effect:
# Test if the right and left sides of the sprite are
# touching different tiles
			if right_tile != left_tile:
# If both tests are true, change the vampire speed to 1
				vampire.speed = SLOW_SPEED
# To Do: Replace the value of vampire.speed

# Delete the vampire sprite when it leaves the screen
		if vampire.rect.x <= 0:
			vampire.kill()

# TO Do: Test if the right side of the vampire sprite is
# on the grid
		if 0 <= vamp_right_side <=10:
			right_tile = tile_row[vamp_right_side]
# Returns no column if the vampire sprite is not on the grid
		else:
			right_tile = None
		
# To Do: Store the location of right_tile

# To Do: Test if the right side of the vampire sprite
# is not on the screen

# To Do: Set the value of right_tile to None

# Update displays
	for vampire in all_vampires:
		vampire.update(GAME_WINDOW)
			
	display.update()

# To Do: Set the frame rate
clock.tick(FRAME_RATE)

#End of main game loop
#----
#Clean up game
pygame.quit()
