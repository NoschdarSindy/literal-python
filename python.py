"""
This is a simple snake game including a snake class.

Game screen width and height are adjustable,
but should be divisible by the dimension 'd' without remainder
"""

import pygame, random

w, h = (600, 400) #width and height of the game window
d = 10 #make the smallest dimensional unit used in the game equal to 10 px
dirs = { "up": (0, -d), "down": (0, d), "left": (-d, 0), "right": (d, 0) } #direction vectors

class Snake():
	"""Lay out a 3 r long snake in the middle of the screen, facing right"""
	def __init__(self):
		self.pos = (w//2, h//2)
		self.path = [(self.pos[0] - i * d, self.pos[1]) for i in range(3)]
		self.dir = 'right'
		self.hungry = True
	
	"""Change the snake's direction"""
	def chDir(self, dir):
		self.dir = dir
	
	"""Move forward by 1 r"""
	def fwd(self):
		if s.hungry: self.path.pop()
		#add the current position and the current direction to calculate the new position
		self.pos = [sum(x) for x in zip(self.pos, dirs[self.dir])]
		self.path.insert(0, self.pos)
		s.hungry = True
		
	def ateFood(self, food):
		if food == self.pos:
			return True
		return False
				
	def bitSelf(self):
		return self.pos in self.path[1:]
		
	def atEdge(self):
		return not (0 <= self.pos[0] < w and 0 <= self.pos[1] < h)	

"""Returns a random position which the given snake does not currently occupy"""
def randPos(snake):
	while True:
		pos = [random.randint(0, w//d -1) * d, random.randint(0, h//d -1) * d]
		if pos not in snake.path: break
	return pos 

#Initialisation	
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake.")
time = pygame.time.Clock()

s = Snake()
food = randPos(s)

while True:
	#Listen for pressed keys
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.KEYDOWN:
			dir = pygame.key.name(e.key)
			if dir in dirs:
				s.chDir(dir)
		elif e.type == pygame.QUIT: exit()
	
	if s.ateFood(food):
		s.hungry = False
		food = randPos(s)
	elif s.bitSelf() or s.atEdge():
		input("Game over! Press enter to exit.")
		break
	
	s.fwd()
	
	win.fill(pygame.Color(255, 255, 255)) #Draw background
	win.fill(pygame.Color(255, 0, 0), pygame.Rect(food[0], food[1], d, d)) #Draw food
	for p in s.path: #Draw snake
		win.fill(pygame.Color(0, 255, 0), pygame.Rect(p[0], p[1], d, d))
		
	pygame.display.flip()
	time.tick(10)
