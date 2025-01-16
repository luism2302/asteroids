from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame
class Asteroids(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y,radius)
		self.add(*self.containers)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return	
		angle = random.uniform(20, 50)
		new_vector_1 = self.velocity.rotate(angle)
		new_vector_2 = self.velocity.rotate(-angle)
		new_radio = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid_1 = Asteroids(self.position.x, self.position.y, new_radio)
		new_asteroid_1.velocity = new_vector_1
		new_asteroid_2 = Asteroids(self.position.x, self.position.y, new_radio)
		new_asteroid_2.velocity = new_vector_2